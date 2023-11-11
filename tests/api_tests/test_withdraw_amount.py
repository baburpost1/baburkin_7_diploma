from tests.conftest import login_session, close_session
from tests.api_tests.utils.links import get_full_api_url
from tests.api_tests.utils.routes import ComboCards
from tests.api_tests.utils.validations import assert_status_code, validate_schema



def test_withdraw_amount(login_session, close_session):
    requests = login_session
    withdraw_url = get_full_api_url(ComboCards.TRANSFER)
    withdraw_positive_amount_response = requests.post(url=withdraw_url,
                                                      params={'user_id': 4424, 'action': 'withdraw', 'amount': 10})
    assert_status_code(withdraw_positive_amount_response.status_code, 400)
    assert withdraw_positive_amount_response.text == '{"detail":"Not enough money"}'

    withdraw_negative_amount_response = requests.post(url=withdraw_url, params={'user_id': 4424, 'action': 'withdraw', 'amount': -10})
    assert_status_code(withdraw_negative_amount_response.status_code, 400)
    assert withdraw_positive_amount_response.text == '{"detail":"Not enough money"}'
