from time import sleep
from selenium import webdriver
from selenium.webdriver.common.by import By


def test_navigation():
    driver = webdriver.Chrome()
    driver.get("https://httpbin.qa-territory.online/")
    sleep(2)

    driver.maximize_window()

    click_button = driver.find_element(By.LINK_TEXT, "HTML Form")
    click_button.click()

    assert "/forms/post" in driver.current_url
    driver.back()

    assert driver.current_url == "https://httpbin.qa-territory.online/"
    sleep(4)

    driver.quit()
