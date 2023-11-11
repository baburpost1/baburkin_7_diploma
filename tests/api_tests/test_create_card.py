import os
from tests.conftest import login_session, close_session
from utils.validations import assert_status_code


def test_create_card(login_session, close_session):
    requests = login_session
    url_create_card = f'https://my.combo.cards/api/cards/'

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
    assert response.text == "{\"detail\":\"Demo user can't create cards\"}"



# залогиниться
# создать карту
# валидировать код ответа
# - [ ]  Значение в *response*.
# - [ ]  Cхема ответа
