from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_dynamic_loading():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get("https://the-internet.herokuapp.com/dynamic_loading/2")

    start_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "#start button")
    ))
    start_button.click()

    text = wait.until(EC.presence_of_element_located(
        (By.ID, "finish")
    ))

    driver.save_screenshot("screenshots/finish_screen_task1.png")

    assert text.text == "Hello World!"
    f"Ожидаемый результат: 'Hello World!', фактический результат'{text.text}'"

    driver.quit()
