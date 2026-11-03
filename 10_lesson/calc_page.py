import allure
from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait


class CalculatorPage:

    DELAY_INPUT = (By.ID, "delay")
    BTN_7 = (By.XPATH, "//span[text()='7']")
    BTN_8 = (By.XPATH, "//span[text()='8']")
    BTN_PLS = (By.XPATH, "//span[text()='+']")
    BTN_RES = (By.XPATH, "//span[text()='=']")
    RESULT = (By.CSS_SELECTOR, "[class='screen']")

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 46)

    @allure.step("Открыть страницу медленного калькулятора")
    def open(self) -> None:
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
        )

    @allure.step("Ввести задержку выполнения равную {time} сек.")
    def input_delay(self, time: str) -> None:
        delay_input = self.wait.until(EC.presence_of_element_located(
            self.DELAY_INPUT
        ))
        delay_input.clear()
        delay_input.send_keys(time)

    @allure.step("Нажать кнопку '7'")
    def click_7(self) -> None:
        btn_7 = self.driver.find_element(*self.BTN_7)
        btn_7.click()

    @allure.step("Нажать кнопку '+'")
    def click_pls(self) -> None:
        btn_pls = self.driver.find_element(*self.BTN_PLS)
        btn_pls.click()

    @allure.step("Нажать кнопку '8'")
    def click_8(self) -> None:
        btn_8 = self.driver.find_element(*self.BTN_8)
        btn_8.click()

    @allure.step("Нажать кнопку '=' для получения результата")
    def click_res(self) -> None:
        btn_res = self.driver.find_element(*self.BTN_RES)
        btn_res.click()

    @allure.step("Дождаться появления результата и получить его текст")
    def assert_res(self) -> str:
        self.wait.until(EC.text_to_be_present_in_element(
            self.RESULT, "15"
        ))
        result = self.driver.find_element(*self.RESULT)
        return result.text
