import allure
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from locators import Locators


class LoginShopPage:

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Открыть страницу авторизации Saucedemo")
    def open(self) -> None:
        self.driver.get("https://www.saucedemo.com/")

    @allure.step("Ввести логин, пароль и выполнить вход в систему")
    def login_input(self) -> None:
        un_input = self.driver.find_element(*Locators.USERNAME_INPUT)
        un_input.send_keys("standard_user")

        pass_input = self.driver.find_element(*Locators.PASS_INPUT)
        pass_input.send_keys("secret_sauce")

        login_btn = self.driver.find_element(*Locators.LOGIN_BTN)
        login_btn.click()


class AddShopPage:

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Добавить рюкзак (Sauce Labs Backpack) в корзину")
    def add_backpack(self) -> None:
        add_bp = self.wait.until(
            EC.element_to_be_clickable(Locators.BTN_CART_BP)
        )
        add_bp.click()

    @allure.step("Добавить футболку (Sauce Labs Bolt T-Shirt) в корзину")
    def add_bolt(self) -> None:
        add_bolt = self.driver.find_element(*Locators.BTN_CART_BOLT)
        add_bolt.click()

    @allure.step("Добавить комбинезон (Sauce Labs Onesie) в корзину")
    def add_onesie(self) -> None:
        add_onesie = self.driver.find_element(*Locators.BTN_CART_ONESIE)
        add_onesie.click()

    @allure.step("Перейти к оформлению заказа (корзина)")
    def click_to_cont(self) -> None:
        to_cont = self.driver.find_element(*Locators.BTN_CART_CONT)
        to_cont.click()


class ChekShopPage:

    def __init__(self, driver: WebDriver) -> None:
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    @allure.step("Нажать кнопку Checkout")
    def click_chekout(self) -> None:
        chekout_btn = self.wait.until(
            EC.element_to_be_clickable(Locators.BTN_CHEKOUT)
        )
        chekout_btn.click()

    @allure.step(
        "Заполнить данные пользователя: имя '{first_name}', фамилия"
        " '{last_name}', индекс '{postal}'"
    )
    def name_input(
        self,
        first_name: str = "Эйлин",
        last_name: str = "Вулфберг",
        postal: str = "395008"
    ) -> None:
        fn_input = self.wait.until(
            EC.presence_of_element_located(Locators.FIRST_NAME_INPUT)
        )
        fn_input.send_keys(first_name)

        ln_input = self.driver.find_element(*Locators.LAST_NAME_INPUT)
        ln_input.send_keys(last_name)

        post_input = self.driver.find_element(*Locators.POST_INPUT)
        post_input.send_keys(postal)

        btn_continue = self.driver.find_element(*Locators.BTN_CONTINUE)
        btn_continue.click()

    @allure.step("Получить общую сумму заказа (Total)")
    def assert_sum(self) -> str:
        self.wait.until(EC.presence_of_element_located(Locators.TOTAL_SUM))
        total_sum = self.driver.find_element(*Locators.TOTAL_SUM)
        return total_sum.text
