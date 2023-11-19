from tests.conftest import login_pp, return_english_language, config_browser
from tests.pages import settings
from selene import browser, be, have, query
from allure import step
import allure


@allure.feature('Смена языка пользователем в настройках')
def test_change_language(login_pp, return_english_language, config_browser):
    settings_page = browser.open(settings.page_url)
    if settings_page.element(settings.header_language).get(query.text) == 'Language':
        with step('Смена языка на RU'):
            settings_page.element(settings.select_language).click()
            settings_page.element(settings.span_russian).click()
        with step('Проверка что язык сменился'):
            settings_page.element(settings.toast_success).should(be.visible)
            settings_page.element(settings.header_language).should(have.text('Язык'))

    elif settings_page.element(settings.header_language).get(query.text) == 'Язык':
        with step('Смена языка на EN'):
            settings_page.element(settings.select_language).click()
            settings_page.element(settings.span_eng).click()
        with step('Проверка что язык сменился'):
            settings_page.element(settings.toast_success).should(be.visible)
            settings_page.element(settings.header_language).should(have.text('Language'))
    else:
        AttributeError
