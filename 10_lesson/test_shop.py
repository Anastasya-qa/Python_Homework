import allure
import pytest
from selenium import webdriver
from shop_page import AddShopPage, ChekShopPage, LoginShopPage


@pytest.fixture
def driver():
    driver = webdriver.Firefox()
    driver.maximize_window()
    yield driver
    driver.quit()


@allure.epic("Интернет-магазин Saucedemo")
@allure.feature("Оформление заказа")
@allure.story("Добавление товаров в корзину и проверка суммы")
@allure.title("Успешное оформление покупки товаров с проверкой итоговой суммы")
@allure.description(
    "Тест проверяет авторизацию пользователя, добавление трех товаров "
    "(Backpack, Bolt T-Shirt, Onesie) в корзину, "
    "заполнение персональных данных на этапе Checkout"
    "и сверку итоговой стоимости заказа (Total: $58.29)."
)
@allure.severity("critical")
@allure.id("SKYPRO-SHOP-10")
def test_shop_cont(driver: webdriver.Firefox) -> None:

    with allure.step("Авторизация пользователя в системе"):
        login = LoginShopPage(driver)
        login.open()
        login.login_input()

    with allure.step("Добавление товаров в корзину и переход к оформлению"):
        add_shop = AddShopPage(driver)
        add_shop.add_backpack()
        add_shop.add_bolt()
        add_shop.add_onesie()
        add_shop.click_to_cont()

    with allure.step("Оформление заказа и проверка итоговой суммы"):
        check_shop = ChekShopPage(driver)
        check_shop.click_chekout()
        check_shop.name_input()
        total_text = check_shop.assert_sum()

    with allure.step("Сравнение полученной суммы с ожидаемой"):
        assert total_text == "Total: $58.29"
