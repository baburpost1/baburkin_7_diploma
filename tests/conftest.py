import pytest
import os
import requests
from selene import browser, be, query
from tests.pages import loginpage, wallet, settings
from selenium import webdriver
from dotenv import load_dotenv


@pytest.fixture(scope='function', autouse=True)
def config_browser():
    driver = webdriver.Chrome()
    browser.config.base_url = 'https://my.combo.cards/'
    browser.driver.set_window_size(width=4000, height=2000)


@pytest.fixture
def login_pp(config_browser):
    load_dotenv()
    login = os.getenv('LOGIN')
    password = os.getenv('PASSWORD')
    pp_login_page = browser.open(loginpage.page_url)
    pp_login_page.element(loginpage.input_username).type(login)
    pp_login_page.element(loginpage.input_password).type(password)
    pp_login_page.element(loginpage.button_submit).click()
    pp_login_page.wait_until(pp_login_page.element(loginpage.logo).should(be.visible))


@pytest.fixture
def del_wallet(config_browser):
    yield
    wallet_page = browser.open(wallet.page_url)
    wallet_page.element(wallet.button_delete_wallet).click()
    wallet_page.element(wallet.button_confirm_delete_wallet).click()
    wallet_page.element(wallet.toast_success2).should(be.visible)


@pytest.fixture
def return_english_language(config_browser):
    yield
    settings_page = browser.open(settings.page_url)
    if settings_page.element(settings.header_language).get(query.text) == 'Язык':
        settings_page.element(settings.select_language).click()
        settings_page.element(settings.span_eng).click()


@pytest.fixture
def login_session():
    load_dotenv()
    login = requests.Session()
    login.post(url=f'{os.getenv("API_BASE_URL")}/login?fingerprint=1650830455',
               data={'username': os.getenv('LOGIN'), 'password': os.getenv('PASSWORD')})
    return login


@pytest.fixture()
def close_session(login_session):
    yield login_session.close()
