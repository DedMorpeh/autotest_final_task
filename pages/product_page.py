from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):
    def add_product_to_basket(self):
        self.should_be_add_to_basket_button()
        add_to_basket_button = self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON)
        add_to_basket_button.click()
        self.solve_quiz_and_get_code()

    def check_product_title_in_added_message(self):
        self.should_be_product_title()
        self.should_be_product_title_in_added_message()
        product_title = self.browser.find_element(*ProductPageLocators.PRODUCT_TITLE)
        product_title_in_added_message = self.browser.find_element(*ProductPageLocators.TITLE_IN_ADDED_MESSAGE)
        assert product_title.text == product_title_in_added_message.text, "Product title in added message is different"

    def check_product_price_in_info_message(self):
        self.should_be_product_price()
        self.should_be_product_price_in_info_message()
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE)
        product_price_in_info_message = self.browser.find_element(*ProductPageLocators.PRICE_IN_INFO_MESSAGE)
        assert product_price.text == product_price_in_info_message.text, "Product price in info message is different"

    def should_be_add_to_basket_button(self):
        assert self.is_element_present(*ProductPageLocators.ADD_TO_BASKET_BUTTON), \
            "Add to basket button is not presented"

    def should_be_product_title(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_TITLE), \
            "Product title is not presented"

    def should_be_product_title_in_added_message(self):
        assert self.is_element_present(*ProductPageLocators.TITLE_IN_ADDED_MESSAGE), \
            "Product title in added message is not presented"

    def should_be_product_price(self):
        assert self.is_element_present(*ProductPageLocators.PRODUCT_PRICE), \
            "Product price is not presented"

    def should_be_product_price_in_info_message(self):
        assert self.is_element_present(*ProductPageLocators.PRICE_IN_INFO_MESSAGE), \
            "Product price in info message is not presented"
