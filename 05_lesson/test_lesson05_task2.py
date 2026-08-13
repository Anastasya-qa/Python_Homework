from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_form_submisson():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/forms/post")

    driver.maximize_window()

    driver.find_element(By.NAME, "custname").send_keys(
        "Ghost"
    )

    click_button = driver.find_element(By.XPATH,
                                       "//button[text()='Submit order']")
    click_button.click()

    url_before = "https://httpbin.qa-territory.online/forms/post"
    assert driver.current_url != url_before

    sleep(4)

    driver.quit()
