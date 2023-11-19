import allure
from selene import browser, be
from tests.pages import loginpage, virtual_cards, card_builder
from tests.conftest import login_pp, config_browser
from allure import step


@allure.feature('Деморежим')
def test_demomode(login_pp, config_browser):
    with step('Проверка уведомления в заголовке о деморежиме'):
        assert browser.element(loginpage.heder_demomode).should(be.visible)
    with step('Заполнение данных для выпуска карты'):
        virtual_cards_page = browser.open(virtual_cards.page_url)
        virtual_cards_page.element(virtual_cards.button_create_new_card).click()

        card_builder_page = browser.open(card_builder.page_url)
        card_builder_page.wait_until(card_builder_page.element('[id="cube-loader"]').should(be.visible))
        card_builder_page.element(card_builder.source_first).click()
        card_builder_page.element(card_builder.input_cart_name).click().type('test')
        card_builder_page.element(card_builder.select_type).click()
        card_builder_page.element(card_builder.limit_type).click()
        card_builder_page.element(card_builder.imput_number).send_keys(10)
        card_builder_page.element(card_builder.select_limit_rule).click()
        card_builder_page.element(card_builder.rule_monthly).click()
        card_builder_page.element(card_builder.input_3d_secure_password).send_keys('12345678')

    with step('Проверка недоступности кнопки создать в окне создания карт'):
        card_builder_page.element(card_builder.button_submit).should(be.disabled)
    with step('Проверка наличия уведомления о демо режиме и просьбы заполнить форму KYC'):
        card_builder_page.element(card_builder.block_verify_acc).should(be.visible)
