from tests.conftest import login_session, close_session
from tests.api_tests.utils.validations import assert_status_code
from tests.api_tests.utils.links import get_full_api_url
from tests.api_tests.utils.routes import ComboCards
import allure
from allure import step


@allure.feature('Создание карты в деморежиме')
def test_create_card(login_session, close_session):
    requests = login_session
    with step('Формирование и отправка запроса'):
        url_create_card = f'{get_full_api_url(ComboCards.CARDS)}'

        body_create_card = {"name": "fdg fdgd", "frequency": "non_recurring", "amount": 10, "expiry_months": 35,
                            "quantity": 1, "note": "",
                            "provider": {"id": 12, "name": "HK Credit Platinum USD (BIN)", "currency": "USD",
                                         "billing_address": "4001 Gagarina",
                                         "card_cost": 2, "top_up_fee": {"value": 1, "percent": 1},
                                         "create_min_deposit": {"limit": 10, "balance": 10}, "max_expiry_months": 35,
                                         "editable_expiry_date": 'true', "no_withdraw": 'false', "no_freeze": 'false',
                                         "monthly_service_fee": 2}, "type": "balance", "secure_3d_password": '12345678',
                            "currency": "USD", "provider_id": 12}

        response = requests.post(url_create_card, json=body_create_card)

    assert_status_code(response.status_code, 400)
    with step('Проверка текста ответа'):
        assert response.text == "{\"detail\":\"Demo user can't create cards\"}"
