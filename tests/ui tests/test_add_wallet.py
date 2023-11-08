from tests.conftest import login_pp, del_wallet, config_browser
from tests.pages import wallet, dashboard
from selene import browser, be
from config import tron_wallet


def test_add_wallet(login_pp, del_wallet, config_browser):
    wallet_page = browser.open(wallet.page_url)
    wallet_page.element(wallet.button_add).click()
    wallet_page.element(wallet.select_blockchain).click()
    wallet_page.element(wallet.blockchain_option).click()
    wallet_page.element(wallet.input_address).send_keys(tron_wallet)
    wallet_page.element(wallet.button_submit).click()
    # Проверить что он появился в списке

    # Проверка того что кошелёк появился в дашборде
    dashboard_page = browser.open(dashboard.page_url)
    dashboard_page.element(dashboard.button_add_trc).click()
    dashboard_page.element(dashboard.select_wallet).click()
    dashboard_page.element(f'//span[contains(text(), \'{tron_wallet}\')]').click()
    dashboard_page.element(dashboard.input_hash).should(be.visible)

    # Проверка что получилось ыбрать этот платёжный метод
    dashboard_page.element(dashboard.input_hash).should(be.visible)