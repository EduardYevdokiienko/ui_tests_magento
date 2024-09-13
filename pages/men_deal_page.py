import allure
from .base_page import BasePage
from .locators import SaleLocators as loc


class MenDealPage(BasePage):
    page_url = '/promotions/men-sale.html'

    @allure.step('Men deal page')
    def check_men_page_opened(self, page_title):
        assert page_title in self.find(loc.MEN_PAGE_TITLE).text
