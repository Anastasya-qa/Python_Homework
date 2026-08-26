from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_color_display():
    driver = webdriver.Firefox()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get\
        ("https://www.saucedemo.com/")

    username_input = driver.find_element(By.ID, "user-name")
    username_input.send_keys("standard_user")

    password_input = driver.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")

    login_btn = driver.find_element(By.ID, "login-button")
    login_btn.click()

    btn_cart_bp = wait.until(EC.presence_of_element_located(
        (By.ID, "add-to-cart-sauce-labs-backpack")
    ))
    btn_cart_bp.click()

    btn_cart_bolt = driver.find_element\
        (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    btn_cart_bolt.click()

    btn_cart_labs = driver.find_element\
        (By.ID, "add-to-cart-sauce-labs-onesie")
    btn_cart_labs.click()

    btn_cart_cont = driver.find_element\
        (By.CSS_SELECTOR, "[class='shopping_cart_link']")
    btn_cart_cont.click()

    btn_chekout = wait.until(EC.presence_of_element_located(
        (By.ID, "checkout")
    ))
    btn_chekout.click()

    first_name_input = wait.until(EC.presence_of_element_located(
        (By.ID, "first-name")
    ))
    first_name_input.send_keys("Эйлин")

    last_name_input = driver.find_element(By.ID, "last-name")
    last_name_input.send_keys("Вулфберг")

    post_input = driver.find_element(By.ID, "postal-code")
    post_input.send_keys("395008")

    btn_continue = driver.find_element(By.ID, "continue")
    btn_continue.click()

    total_sum = wait.until(EC.presence_of_element_located(
        (By.CSS_SELECTOR, "[class='summary_total_label']")
    ))
    driver.save_screenshot("screenshots/total_test_3.png")
    assert total_sum.text == 'Total: $58.29'

    driver.quit()
