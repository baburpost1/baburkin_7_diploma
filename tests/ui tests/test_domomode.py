from selene import browser, be
import config
from tests.pages import loginpage, virtual_cards, card_builder
from tests.conftest import login_pp, config_browser


def test_demomode(login_pp, config_browser):
    # Проверка что есть уведомлениео деморежиме
    assert browser.element(loginpage.heder_demomode).should(be.visible)
    # проверяем что не можем создать карты
    virtual_cards_page = browser.open(virtual_cards.page_url)
    virtual_cards_page.element(virtual_cards.button_create_new_card).click()

    card_builder_page = browser.open(card_builder.page_url)
    card_builder_page.wait_until(card_builder_page.element('[id="cube-loader"]').should(be.visible))
    card_builder_page.element(card_builder.input_cart_name).click().type('test')
    card_builder_page.element(card_builder.select_source).click()
    card_builder_page.element(card_builder.input_provider).send_keys(474359)
    card_builder_page.element(card_builder.source_first).click()
    card_builder_page.element(card_builder.select_type).click()
    card_builder_page.element(card_builder.limit_type).click()
    card_builder_page.element(card_builder.imput_number).send_keys(10)
    card_builder_page.element(card_builder.select_limit_rule).click()
    card_builder_page.element(card_builder.rule_monthly).click()
    card_builder_page.element(card_builder.input_3d_secure_password).send_keys('12345678')

    # Проверка что кнопка недоступна и плашка на месте
    card_builder_page.element(card_builder.button_submit).should(be.disabled)
    card_builder_page.element(card_builder.block_verify_acc).should(be.visible)
