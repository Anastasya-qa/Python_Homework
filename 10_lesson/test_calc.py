import allure
import pytest
from calc_page import CalculatorPage
from selenium import webdriver


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.epic("Веб-инструменты")
@allure.feature("Медленный калькулятор")
@allure.story("Вычисление суммы с задержкой времени")
@allure.title("Успешное сложение чисел 7 и 8 с учетом задержки")
@allure.description(
    "Тест открывает страницу калькулятора, "
    "устанавливает задержку в 45 секунд, "
    "выполняет математическую операцию 7 + 8 и проверяет, "
    "что на экране "
    "появляется корректный результат '15'."
)
@allure.severity("normal")
@allure.id("SKYPRO-CALC-10")
def test_calculator(driver: webdriver.Chrome) -> None:
    calc_page = CalculatorPage(driver)

    with allure.step("Открытие калькулятора и настройка задержки"):
        calc_page.open()
        calc_page.input_delay("45")

    with allure.step("Ввод математического выражения (7 + 8)"):
        calc_page.click_7()
        calc_page.click_pls()
        calc_page.click_8()
        calc_page.click_res()

    with allure.step("Проверка итогового результата"):
        result_text = calc_page.assert_res()
        assert result_text == "15"
