from tests.conftest import login_pp, return_english_language, config_browser
from tests.pages import settings
from selene import browser, be, have, query


def test_change_language(login_pp, return_english_language, config_browser):
    settings_page = browser.open(settings.page_url)
    if settings_page.element(settings.header_language).get(query.text) == 'Language':
        settings_page.element(settings.select_language).click()
        settings_page.element(settings.span_russian).click()
        # Проверка что язык сменился
        settings_page.element(settings.toast_success).should(be.visible)
        settings_page.element(settings.header_language).should(have.text('Язык'))

    elif settings_page.element(settings.header_language).get(query.text) == 'Язык':
        settings_page.element(settings.select_language).click()
        settings_page.element(settings.span_eng).click()
        # Проверка что язык сменился
        settings_page.element(settings.toast_success).should(be.visible)
        settings_page.element(settings.header_language).should(have.text('Language'))
    else:
        AttributeError
