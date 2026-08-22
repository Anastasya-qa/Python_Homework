from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_session_storage_auth():
    driver = webdriver.Chrome()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get("https://gitflic.ru/")

    driver.add_cookie({
            "name": "SESSION",
            "value": "ZjZmM2E2MmQtN2M4NS00Njk1LWJiYWYtZmZkNjNkYjg0Yzg5",
            "domain": "gitflic.ru"
        })

    driver.add_cookie({
        "name": "cookiesAccepted",
        "value": "true",
        "domain": "gitflic.ru"
        })
    driver.refresh()
    driver.get("https://gitflic.ru/user/anastasya_qa")

    current_url_user_1 = driver.current_url

    driver.delete_cookie("SESSION")

    driver.add_cookie({
            "name": "SESSION",
            "value": "YTUzZTZhOWUtODc2OC00M2UzLTk4MDAtODFiZmViZDUwODgz",
            "domain": "gitflic.ru"
        })
    driver.refresh()
    driver.get("https://gitflic.ru/user/naya_qa")

    current_url_user_2 = driver.current_url

    assert current_url_user_1 != current_url_user_2

    driver.quit()
