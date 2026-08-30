import pytest
from selenium import webdriver
from pages.shop_page import LoginShopPage
from pages.shop_page import AddShopPage
from pages.shop_page import ChekShopPage
# для запуска:
# pytest 07_lesson/tests/test_shop.py


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shop_cont(driver):
    login = LoginShopPage(driver)
    login.open()
    login.login_input()

    add_shop = AddShopPage(driver)
    add_shop.add_backpack()
    add_shop.add_bolt()
    add_shop.add_onesie()
    add_shop.click_to_cont()

    check_shop = ChekShopPage(driver)
    check_shop.click_chekout()
    check_shop.name_input()
    check_shop.assert_sum()

    assert check_shop.assert_sum() == 'Total: $58.29'
