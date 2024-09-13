import allure
from pages.base_page import BasePage
from pages.locators import SaleLocators as loc


class WomenDealPage(BasePage):
    page_url = '/promotions/women-sale.html'

    @allure.step('Women deal page')
    def check_women_page_opened(self, page_title):
        assert page_title in self.find(loc.WOMEN_PAGE_TITLE).text
