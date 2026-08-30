from selenium.webdriver.common.by import By


class Locators:

    USERNAME_INPUT = (By.ID, "user-name")
    PASS_INPUT = (By.ID, "password")
    LOGIN_BTN = (By.ID, "login-button")
    BTN_CART_BP = (By.ID, "add-to-cart-sauce-labs-backpack")
    BTN_CART_BOLT = (
            By.ID, "add-to-cart-sauce-labs-bolt-t-shirt"
            )
    BTN_CART_ONESIE = (
            By.ID, "add-to-cart-sauce-labs-onesie"
            )
    BTN_CART_CONT = (
            By.CSS_SELECTOR, "[class='shopping_cart_link']"
            )
    BTN_CHEKOUT = (By.ID, "checkout")
    FIRST_NAME_INPUT = (By.ID, "first-name")
    LAST_NAME_INPUT = (By.ID, "last-name")
    POST_INPUT = (By.ID, "postal-code")
    BTN_CONTINUE = (By.ID, "continue")
    TOTAL_SUM = (By.CSS_SELECTOR, "[class='summary_total_label']")
