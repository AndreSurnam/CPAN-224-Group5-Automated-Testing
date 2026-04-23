from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

# TC11
# Valid login, then navigate to Timesheet page and Punch In page


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


def go_to_timesheet_page(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet")

    WebDriverWait(driver, 20).until(
        EC.url_contains("/web/index.php/time/viewEmployeeTimesheet")
    )

    print("PASS - Timesheet page opened")
    print("Current URL:", driver.current_url)


def go_to_punchin_page(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/attendance/punchIn")

    WebDriverWait(driver, 20).until(
        EC.url_contains("/web/index.php/attendance/punchIn")
    )

    print("PASS - Punch In page opened")
    print("Current URL:", driver.current_url)


if __name__ == "__main__":
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    try:
        login_func(driver, username="Admin", pw="admin123")
        go_to_timesheet_page(driver)
        time.sleep(2)
        go_to_punchin_page(driver)
        time.sleep(5)

    finally:
        driver.quit()