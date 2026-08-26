from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def test_color_display():
    driver = webdriver.Edge()
    wait = WebDriverWait(driver, 10)
    driver.maximize_window()
    driver.get\
        ("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    first_name_input = wait.until(EC.presence_of_element_located(
        (By.NAME, "first-name")
    ))
    first_name_input.send_keys("Иван")

    last_name_input = driver.find_element(By.NAME, "last-name")
    last_name_input.send_keys("Петров")

    address_input = driver.find_element(By.NAME, "address")
    address_input.send_keys("Ленина, 55-3")

    city_input = driver.find_element(By.NAME, "city")
    city_input.send_keys("Москва")

    country_input = driver.find_element(By.NAME, "country")
    country_input.send_keys("Россия")

    email_input = driver.find_element(By.NAME, "e-mail")
    email_input.send_keys("test@skypro.com")

    num_phone_input = driver.find_element(By.NAME, "phone")
    num_phone_input.send_keys("+7985899998787")

    job_input = driver.find_element(By.NAME, "job-position")
    job_input.send_keys("QA")

    company_input = driver.find_element(By.NAME, "company")
    company_input.send_keys("SkyPro")

    submit_button = wait.until(EC.element_to_be_clickable(
        (By.CSS_SELECTOR, "button[type='submit']")
    ))
    submit_button.click()

    zip_code_color = wait.until(EC.presence_of_element_located(
        (By.ID, "zip-code")
    ))
    bg_danger = zip_code_color.value_of_css_property('background-color')
    assert bg_danger == 'rgba(248, 215, 218, 1)' in bg_danger

    fields = ["first-name",
              "last-name",
              "address",
              "city",
              "country",
              "e-mail",
              "phone",
              "job-position",
              "company"]

    for field_id in fields:
        field_element = driver.find_element(By.ID, field_id)

    bg_success = field_element.value_of_css_property("border-color")
    assert bg_success == 'rgb(186, 219, 204)' in bg_success

    driver.save_screenshot("screenshots/field_color_test_1.png")

    driver.quit()
