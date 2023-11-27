from tests.conftest import login_session, close_session
from tests.api_tests.utils.links import get_full_api_url
from tests.api_tests.utils.routes import ComboCards
from tests.api_tests.utils.validations import assert_status_code, validate_schema
from allure import step
import allure


@allure.feature('Проверка доступной информации для пользователя')
def test_check_users_info(login_session, close_session):
    requests = login_session
    with step('Получаем список всех доступных пользователей'):
        all_users_url = get_full_api_url(ComboCards.USERS)
        all_users = requests.get(url=all_users_url, params={'sorting': 'id', 'order': 'desc', 'page': 1, 'count': 25})
    assert_status_code(all_users.status_code, 200)
    for user in all_users.json()['objects']:
        validate_schema(user, 'user.json')

    with step('Получение списка всех подчинённых'):
        slave_user_id = []
        for user in all_users.json()['objects']:
            if user['role'] == 2:
                slave_user_id.append(user['id'])
        fin_manager = slave_user_id[0]
        manage_user_slave_url = f'{get_full_api_url(ComboCards.USERS)}'
        manage_user_slave_response = requests.get(manage_user_slave_url, params={'user_id': fin_manager})
        assert_status_code(manage_user_slave_response.status_code, 200)
        user = manage_user_slave_response.json()['objects']
        assert len(user) == 1
        validate_schema(user[0], 'user.json')

    with step('Проверка что подчинённый не может получить информацию по головной группе'):
        users_not_from_your_command_response = requests.get(manage_user_slave_url, params={'user_id': 1})
        assert_status_code(users_not_from_your_command_response.status_code, 200)
        assert len(users_not_from_your_command_response.json()['objects']) == 0
