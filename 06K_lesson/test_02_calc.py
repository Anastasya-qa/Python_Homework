from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_calculator():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 45)
    driver.maximize_window()
    driver.get(
        "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

    delay_button = wait.until(EC.presence_of_element_located(
        (By.ID, "delay")
    ))
    delay_button.clear()
    delay_button.send_keys("45")

    button_7 = driver.find_element(By.XPATH, "//span[text()='7']")
    button_7.click()

    button_pls = driver.find_element(By.XPATH, "//span[text()='+']")
    button_pls.click()

    button_8 = driver.find_element(By.XPATH, "//span[text()='8']")
    button_8.click()

    button_res = driver.find_element(By.XPATH, "//span[text()='=']")
    button_res.click()

    result = wait.until(EC.text_to_be_present_in_element(
        (By.CSS_SELECTOR, "[class='screen']"), '15')
        )
    assert result

    driver.quit()
