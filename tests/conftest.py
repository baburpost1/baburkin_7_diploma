import pytest
import os
import requests
from selene import browser, be, query
from tests.pages import loginpage, wallet, settings
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from dotenv import load_dotenv
from tests.utils import attach


@pytest.fixture(scope='function', autouse=True)
def config_browser():
    driver = webdriver.Chrome()
    browser.config.base_url = 'https://my.combo.cards/'

    def setup_browser():
        # Список всех доступных парамеров https://peter.sh/experiments/chromium-command-line-switches/

        browser.config.window_height = 1400
        browser.config.window_width = 1600
        browser_version = "100.0"
        options = Options()
        selenoid_capabilities = {
            "browserName": "chrome",
            "browserVersion": browser_version,
            "selenoid:options": {
                "enableVNC": True,
                "enableVideo": True
            }
        }
        login = os.getenv('SELEN_LOGIN')
        password = os.getenv('SELEN_PASSWORD')
        options.capabilities.update(selenoid_capabilities)
        driver = webdriver.Remote(
            command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
            options=options
        )

        browser.config.driver = driver

        yield

        attach.add_html(browser)
        attach.add_screenshot(browser)
        # attach.add_video(browser)
        attach.add_logs(browser)

        browser.quit()


@pytest.fixture()
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
    login.post(url=f'{os.getenv("API_BASE_URL")}/auth/login?fingerprint=1650830455',
               data={'username': os.getenv('LOGIN'), 'password': os.getenv('PASSWORD')})
    return login


@pytest.fixture()
def close_session(login_session):
    yield login_session.close()
