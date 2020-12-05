from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    empty_basket_text_dict = {
        "ar": "سلة التسوق فارغة",
        "ca": "La seva cistella està buida.",
        "cs": "Váš košík je prázdný.",
        "da": "Din indkøbskurv er tom.",
        "de": "Ihr Warenkorb ist leer.",
        "en": "Your basket is empty.",
        "en-US": "Your basket is empty.",
        "el": "Το καλάθι σας είναι άδειο.",
        "es": "Tu carrito esta vacío.",
        "fi": "Korisi on tyhjä",
        "fr": "Votre panier est vide.",
        "it": "Il tuo carrello è vuoto.",
        "ko": "장바구니가 비었습니다.",
        "nl": "Je winkelmand is leeg",
        "pl": "Twój koszyk jest pusty.",
        "pt": "O carrinho está vazio.",
        "pt-br": "Sua cesta está vazia.",
        "ro": "Cosul tau este gol.",
        "ru": "Ваша корзина пуста",
        "sk": "Váš košík je prázdny",
        "uk": "Ваш кошик пустий.",
        "zh-cn": "Your basket is empty.",
    }

    def should_not_be_products_form(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_FORM), \
            "Products form is presented, but should not be"

    def should_be_empty_basket_text_element(self):
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET_TEXT), \
            "Empty basket text element is not presented, but should be"

    def should_be_empty_basket_text(self):
        self.should_be_empty_basket_text_element()
        empty_basket_text_element = self.browser.find_element(*BasketPageLocators.EMPTY_BASKET_TEXT)
        language = self.get_current_language()
        assert empty_basket_text_element.text.startswith(self.empty_basket_text_dict[language]), \
            "Empty basket text is not presented"
