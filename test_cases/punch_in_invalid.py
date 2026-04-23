from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time


# Duplicate Punch In Prevention


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


def go_to_punch_page(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/time/viewEmployeeTimesheet")
    WebDriverWait(driver, 20).until(
        EC.url_contains("/web/index.php/time/viewEmployeeTimesheet")
    )

    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/attendance/punchIn")
    WebDriverWait(driver, 20).until(
        EC.url_contains("/web/index.php/attendance/")
    )


def get_submit_button(driver):
    return WebDriverWait(driver, 20).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, "button[type='submit']"))
    )


def get_submit_text(driver):
    return get_submit_button(driver).text.strip().lower()


def add_note(driver, text):
    note_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "textarea"))
    )
    note_box.clear()
    note_box.send_keys(text)


def punch_in_if_needed(driver):
    go_to_punch_page(driver)
    button_text = get_submit_text(driver)

    if "in" in button_text:
        add_note(driver, "Initial punch in for duplicate test")
        get_submit_button(driver).click()
        time.sleep(3)
        print("Initial punch in completed")
    else:
        print("User was already punched in")


def duplicate_punchin_test(driver):
    go_to_punch_page(driver)

    current_url = driver.current_url
    button_text = get_submit_text(driver)

    print("Current URL before duplicate test:", current_url)
    print("Current button text:", button_text)


    if "out" in button_text or "punchOut" in current_url:
        print("PASS - System prevents duplicate punch in by keeping user in punched-in state")
    else:
        print("FAIL - User is still able to access a Punch In state while already punched in")

    try:
        message = WebDriverWait(driver, 5).until(
            EC.presence_of_element_located((
                By.XPATH,
                "//*[contains(text(),'Overlapping') or contains(text(),'Invalid') or contains(text(),'Already')]"
            ))
        )
        print("System message found:", message.text)
    except TimeoutException:
        print("No visible validation message found, but state-based prevention is still valid")

    input("Press Enter to close the browser...")


if __name__ == "__main__":
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    try:
        login_func(driver, username="Admin", pw="admin123")
        punch_in_if_needed(driver)
        duplicate_punchin_test(driver)
    finally:
        driver.quit()