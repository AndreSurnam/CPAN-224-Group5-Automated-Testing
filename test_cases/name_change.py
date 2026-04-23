from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# TS_015
# Update Employee Name to TEST TEST TEST


def login_func(driver, username, pw):
    driver.get("https://opensource-demo.orangehrmlive.com/")

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

    user_nm = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    user_nm.clear()
    password.clear()

    user_nm.send_keys(username)
    password.send_keys(pw)
    login_btn.click()

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//h6[text()='Dashboard']"))
    )


def go_to_my_info(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/pim/viewPersonalDetails/empNumber/7")

    WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.XPATH, "//h6[text()='Personal Details']"))
    )


def wait_for_loader_to_disappear(driver):
    try:
        WebDriverWait(driver, 20).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "oxd-form-loader"))
        )
    except:
        pass


def replace_text(driver, xpath, value):
    wait_for_loader_to_disappear(driver)

    field = WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.XPATH, xpath))
    )

    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", field)
    time.sleep(0.5)

    field.click()
    time.sleep(0.5)
    field.send_keys(Keys.CONTROL, "a")
    time.sleep(0.3)
    field.send_keys(Keys.BACKSPACE)
    time.sleep(0.3)
    field.send_keys(value)
    time.sleep(0.5)


def update_employee_name(driver):
    first_name_xpath = "//input[@name='firstName']"
    middle_name_xpath = "//input[@name='middleName']"
    last_name_xpath = "//input[@name='lastName']"

    replace_text(driver, first_name_xpath, "TEST")
    replace_text(driver, middle_name_xpath, "TEST")
    replace_text(driver, last_name_xpath, "TEST")

    first_name = driver.find_element(By.NAME, "firstName")
    middle_name = driver.find_element(By.NAME, "middleName")
    last_name = driver.find_element(By.NAME, "lastName")

    print("First name field now:", first_name.get_attribute("value"))
    print("Middle name field now:", middle_name.get_attribute("value"))
    print("Last name field now:", last_name.get_attribute("value"))

    save_buttons = driver.find_elements(By.CSS_SELECTOR, "button[type='submit']")
    save_buttons[0].click()

    time.sleep(3)

    print("Updated employee name fields")
    print("Current URL:", driver.current_url)

    input("Press Enter to close the browser...")


if __name__ == "__main__":
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    try:
        login_func(driver, username="Admin", pw="admin123")
        go_to_my_info(driver)
        update_employee_name(driver)
    finally:
        driver.quit()