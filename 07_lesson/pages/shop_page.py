from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators import Locators
# в этом тесте я решила добавить отдельный класс для локаторов


class LoginShopPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open(self):
        self.driver.get("https://www.saucedemo.com/")

    def login_input(self):
        un_input = self.driver.find_element(*Locators.USERNAME_INPUT)
        un_input.send_keys("standard_user")

        pass_input = self.driver.find_element(*Locators.PASS_INPUT)
        pass_input.send_keys("secret_sauce")

        login_btn = self.driver.find_element(*Locators.LOGIN_BTN)
        login_btn.click()


class AddShopPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def add_backpack(self):
        add_bp = self.wait.until(EC.element_to_be_clickable(
            Locators.BTN_CART_BP
        ))
        add_bp.click()

    def add_bolt(self):
        add_bolt = self.driver.find_element(*Locators.BTN_CART_BOLT)
        add_bolt.click()

    def add_onesie(self):
        add_onesie = self.driver.find_element(*Locators.BTN_CART_ONESIE)
        add_onesie.click()

    def click_to_cont(self):
        to_cont = self.driver.find_element(*Locators.BTN_CART_CONT)
        to_cont.click()


class ChekShopPage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def click_chekout(self):
        chekout_btn = self.wait.until(EC.element_to_be_clickable(
            Locators.BTN_CHEKOUT
        ))
        chekout_btn.click()

    def name_input(self):
        fn_input = self.wait.until(EC.presence_of_element_located(
            Locators.FIRST_NAME_INPUT
        ))
        fn_input.send_keys("Эйлин")

        ln_input = self.driver.find_element(*Locators.LAST_NAME_INPUT)
        ln_input.send_keys("Вулфберг")

        post_input = self.driver.find_element(*Locators.POST_INPUT)
        post_input.send_keys("395008")

        btn_continue = self.driver.find_element(*Locators.BTN_CONTINUE)
        btn_continue.click()

    def assert_sum(self):
        self.wait.until(EC.presence_of_element_located(
            Locators.TOTAL_SUM
        ))
        total_sum = self.driver.find_element(*Locators.TOTAL_SUM)
        return total_sum.text
