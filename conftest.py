import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from .pages.create_nc_account_page import CreateAccountPage
from .pages.account_page import AccountPage
from .pages.ef_collection_page import EcoFriendlyCollectionPage
from .pages.card_page import CartPage
from .pages.sale_page import SalePage
from .pages.men_deal_page import MenDealPage
from .pages.women_deal_page import WomenDealPage
from .pages.acc_error_page import AccountErrorPage


@pytest.fixture()
def driver():
    options = Options()
    options.add_argument('--headless')
    options.add_argument('--no-sandbox')
    options.add_argument('--disable-dev-shm-usage')
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.implicitly_wait(5)
    yield driver
    driver.quit()


@pytest.fixture()
def create_account_page(driver):
    return CreateAccountPage(driver)


@pytest.fixture()
def account_page(driver):
    return AccountPage(driver)


@pytest.fixture()
def ef_collection_page(driver):
    return EcoFriendlyCollectionPage(driver)


@pytest.fixture()
def card_page(driver):
    return CartPage(driver)


@pytest.fixture()
def sale_page(driver):
    return SalePage(driver)


@pytest.fixture()
def men_deal_page(driver):
    return MenDealPage(driver)


@pytest.fixture()
def women_deal_page(driver):
    return WomenDealPage(driver)


@pytest.fixture()
def ac_error_page(driver):
    return AccountErrorPage(driver)
