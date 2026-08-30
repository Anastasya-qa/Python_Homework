from pages.calc_page import CalculatorPage
from selenium import webdriver
import pytest
# для запуска:
# pytest 07_lesson/tests/test_calc.py


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_calculator(driver):
    calc_page = CalculatorPage(driver)

    calc_page.open()
    calc_page.input_delay("45")
    calc_page.click_7()
    calc_page.click_pls()
    calc_page.click_8()
    calc_page.click_res()

    assert calc_page.assert_res() == "15"
