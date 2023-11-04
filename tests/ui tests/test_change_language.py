from tests.conftest import login_pp
from tests.pages import settings
from selene import browser, be, have
from config import ui_base_url


def test_change_language(login_pp):
    settings_page = browser.open(f'{ui_base_url}/{settings.page_url}')
    if settings_page.element(settings.header_language).should(have.text('Language')):
        settings_page.element(settings.select_language).click()
        settings_page.element(settings.span_russian).click()
        # Проверка что язык сменился
        settings_page.element(settings.toast_success).should(be.visible)
        settings_page.element(settings.header_language).should(have.text('Язык'))

    elif settings_page.element(settings.header_language).should(have.text('Язык')):
        settings_page.element(settings.select_language).click()
        settings_page.element(settings.span_eng).click()
        # Проверка что язык сменился
        settings_page.element(settings.toast_success).should(be.visible)
        settings_page.element(settings.header_language).should(have.text('Language'))
    else:
        AttributeError
