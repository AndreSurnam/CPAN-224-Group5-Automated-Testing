from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time

# TC - Valid Punch In Date

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


def go_to_punchin_page(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet")
    WebDriverWait(driver, 20).until(
        EC.url_contains("/web/index.php/time/viewEmployeeTimesheet")
    )

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/attendance/punchIn")
    WebDriverWait(driver, 20).until(
        EC.url_contains("/web/index.php/attendance/punchIn")
    )


def valid_punchin_date_test(driver):
    wait = WebDriverWait(driver, 20)

    valid_date = "2026-04-05"

    date_xpath = "//label[text()='Date']/../following-sibling::div//input"
    time_xpath = "//label[text()='Time']/../following-sibling::div//input"
    note_xpath = "//textarea"
    submit_xpath = "//button[@type='submit']"

    # Wait for page pieces
    wait.until(EC.element_to_be_clickable((By.XPATH, date_xpath)))
    wait.until(EC.presence_of_element_located((By.XPATH, time_xpath)))
    wait.until(EC.presence_of_element_located((By.XPATH, note_xpath)))

    # Re-find right before use
    date_input = driver.find_element(By.XPATH, date_xpath)
    note_box = driver.find_element(By.XPATH, note_xpath)

    date_input.send_keys(Keys.CONTROL, "a")
    date_input.send_keys(Keys.BACKSPACE)
    date_input.send_keys(valid_date)
    date_input.send_keys(Keys.TAB)

    note_box.clear()
    note_box.send_keys("Valid punch in date test")

    time.sleep(1)

    submit_btn = wait.until(
        EC.element_to_be_clickable((By.XPATH, submit_xpath))
    )
    submit_btn.click()

    time.sleep(3)

    print("TC executed")
    print("Entered valid date:", valid_date)
    print("Current URL:", driver.current_url)

    try:
        error_msg = driver.find_element(By.XPATH, "//*[contains(text(),'Overlapping') or contains(text(),'Invalid') or contains(text(),'Required')]")
        print("Message found:", error_msg.text)
    except:
        print("No visible validation message found")


if __name__ == "__main__":
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    try:
        login_func(driver, username="Admin", pw="admin123")
        go_to_punchin_page(driver)
        valid_punchin_date_test(driver)
        time.sleep(5)
    finally:
        driver.quit()