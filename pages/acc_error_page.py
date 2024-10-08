import allure
from .base_page import BasePage
from .locators import CartLocators as loc


class AccountErrorPage(BasePage):
    page_url = None

    @allure.step('Add to wish list without registration')
    def add_to_wish_list_failed(self, error_massage):
        assert error_massage in self.find(loc.WISH_LIST_ERROR).text
