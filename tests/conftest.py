import pytest
from selene import browser, be
from config import ui_base_url, LOGIN, PASSWORD
from tests.pages import loginpage

@pytest.fixture
def login_pp():
    pp_login_page = browser.open(f'{ui_base_url}/overview?lg=1')
    pp_login_page.element(loginpage.input_username).type(LOGIN)
    pp_login_page.element(loginpage.input_password).type(PASSWORD)
    pp_login_page.element(loginpage.button_submit).click()
    pp_login_page.wait_until(pp_login_page.element(loginpage.logo).should(be.visible))
