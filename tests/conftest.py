import pytest
from selene import browser, be, query
from config import ui_base_url, LOGIN, PASSWORD
from tests.pages import loginpage, wallet, settings

@pytest.fixture
def login_pp():
    pp_login_page = browser.open(f'{ui_base_url}/{loginpage.page_url}')
    pp_login_page.element(loginpage.input_username).type(LOGIN)
    pp_login_page.element(loginpage.input_password).type(PASSWORD)
    pp_login_page.element(loginpage.button_submit).click()
    pp_login_page.wait_until(pp_login_page.element(loginpage.logo).should(be.visible))

@pytest.fixture
def del_wallet():
    yield
    wallet_page = browser.open(f'{ui_base_url}/{wallet.page_url}')
    wallet_page.element(wallet.button_delete_wallet).click()
    wallet_page.element(wallet.button_confirm_delete_wallet).click()
    wallet_page.element(wallet.toast_success2).should(be.visible)

@pytest.fixture
def return_english_language():
    yield
    settings_page = browser.open(f'{ui_base_url}/{settings.page_url}')
    if settings_page.element(settings.header_language).get(query.text) == 'Язык':
        settings_page.element(settings.select_language).click()
        settings_page.element(settings.span_eng).click()