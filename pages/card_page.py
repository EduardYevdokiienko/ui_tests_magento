from .base_page import BasePage
from .locators import CartLocators as loc


class CartPage(BasePage):
    page_url = None

    def check_product_in_cart(self, product_name):
        assert product_name in self.find(loc.PRODUCT_IN_CARD).text

    def check_price_in_cart(self, product_price):
        assert product_price in self.find(loc.PRODUCT_PRICE_IN_CARD).text
