from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:

    DELAY_INPUT = (By.ID, "delay")
    BTN_7 = (By.XPATH, "//span[text()='7']")
    BTN_8 = (By.XPATH, "//span[text()='8']")
    BTN_PLS = (By.XPATH, "//span[text()='+']")
    BTN_RES = (By.XPATH, "//span[text()='=']")
    RESULT = (By.CSS_SELECTOR, "[class='screen']")

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 46)

    def open(self):
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/"
            "slow-calculator.html"
            )

    def input_delay(self, time):
        delay_input = self.wait.until(EC.presence_of_element_located(
            self.DELAY_INPUT
        ))
        delay_input.clear()
        delay_input.send_keys(time)

    def click_7(self):
        btn_7 = self.driver.find_element(*self.BTN_7)
        btn_7.click()

    def click_8(self):
        btn_8 = self.driver.find_element(*self.BTN_8)
        btn_8.click()

    def click_pls(self):
        btn_pls = self.driver.find_element(*self.BTN_PLS)
        btn_pls.click()

    def click_res(self):
        btn_res = self.driver.find_element(*self.BTN_RES)
        btn_res.click()

    def assert_res(self):
        self.wait.until(EC.text_to_be_present_in_element(
            self.RESULT, "15"
        ))
        result = self.driver.find_element(*self.RESULT)
        return result.text
