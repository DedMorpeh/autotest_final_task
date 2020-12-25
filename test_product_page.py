import time
import pytest
from .pages.product_page import ProductPage
from .pages.basket_page import BasketPage
from .pages.login_page import LoginPage


DEFAULT_PRODUCT_LINK = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/"
LOGIN_LINK = "http://selenium1py.pythonanywhere.com/accounts/login/"


@pytest.mark.need_review
@pytest.mark.parametrize('link', [
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
    pytest.param(
        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
        marks=pytest.mark.xfail
    ),
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
    "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"
])
def test_guest_can_add_product_to_basket(browser, link):
    page = ProductPage(browser, link)
    page.open()
    with_quiz_alert = "promo=offer" in browser.current_url
    page.add_product_to_basket(with_quiz=with_quiz_alert)
    page.check_product_title_in_added_message()
    page.check_product_price_in_info_message()


def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
    page = ProductPage(browser, DEFAULT_PRODUCT_LINK)
    page.open()
    page.add_product_to_basket()
    page.should_not_be_success_message()


def test_guest_cant_see_success_message(browser):
    page = ProductPage(browser, DEFAULT_PRODUCT_LINK)
    page.open()
    page.should_not_be_success_message()


def test_message_disappeared_after_adding_product_to_basket(browser):
    page = ProductPage(browser, DEFAULT_PRODUCT_LINK)
    page.open()
    page.add_product_to_basket()
    page.check_is_success_message_disappeared()


def test_guest_should_see_login_link_on_product_page(browser):
    page = ProductPage(browser, DEFAULT_PRODUCT_LINK)
    page.open()
    page.should_be_login_link()


@pytest.mark.need_review
def test_guest_can_go_to_login_page_from_product_page(browser):
    page = ProductPage(browser, DEFAULT_PRODUCT_LINK)
    page.open()
    page.should_be_login_link()
    page.go_to_login_page()


@pytest.mark.need_review
def test_guest_cant_see_product_in_basket_opened_from_product_page(browser):
    page = ProductPage(browser, DEFAULT_PRODUCT_LINK)
    page.open()
    page.go_to_basket_page()
    basket_page = BasketPage(browser, browser.current_url)
    basket_page.should_not_be_products_form()
    basket_page.should_be_empty_basket_text()


@pytest.mark.user_add_to_basket
class TestUserAddToBasketFromProductPage():
    @pytest.fixture(autouse=True)
    def setup(self, browser):
        login_page = LoginPage(browser, LOGIN_LINK)
        login_page.open()
        user_email = str(time.time()) + "@fakemail.org"
        user_password = str(time.time())
        login_page.register_new_user(user_email, user_password)
        login_page.should_be_authorized_user()

    @pytest.mark.need_review
    def test_user_can_add_product_to_basket(self, browser):
        page = ProductPage(browser, DEFAULT_PRODUCT_LINK)
        page.open()
        page.add_product_to_basket()
        page.check_product_title_in_added_message()
        page.check_product_price_in_info_message()

    def test_user_cant_see_success_message(self, browser):
        page = ProductPage(browser, DEFAULT_PRODUCT_LINK)
        page.open()
        page.should_not_be_success_message()
