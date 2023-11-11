from tests.conftest import login_session, close_session
from tests.api_tests.utils.links import get_full_api_url
from tests.api_tests.utils.routes import ComboCards
from tests.api_tests.utils.validations import assert_status_code


def test_exchange_money(login_session, close_session):
    requests = login_session
    convert_url = get_full_api_url(ComboCards.CONVERT)
    convert_response = requests.get(url=convert_url,
                                    params={'from_currency': 'USD', 'to_currency': 'HKD', 'reverse': 'false',
                                            'amount': 10})
    assert_status_code(convert_response.status_code, 400)
    assert convert_response.text ==  '{"detail":"Not enough money"}'

def test_convert_money_negative_amount(login_session, close_session):
    requests = login_session
    convert_url = get_full_api_url(ComboCards.CONVERT)
    convert_response = requests.get(url=convert_url,
                                    params={'from_currency': 'USD', 'to_currency': 'HKD', 'reverse': 'false',
                                            'amount': -10})
    assert_status_code(convert_response.status_code, 400)
    assert convert_response.text == '{"detail":"Amount must be greater then 1 USD"}'
