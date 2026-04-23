from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, StaleElementReferenceException
import time

# TS_014
# Valid Punch Out
# Punch out date/time is set after 2026-04-05


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


def wait_for_loader_to_disappear(driver):
    try:
        WebDriverWait(driver, 20).until(
            EC.invisibility_of_element_located((By.CLASS_NAME, "oxd-form-loader"))
        )
    except:
        pass


def go_to_punch_page(driver):
    driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/attendance/punchIn")
    WebDriverWait(driver, 20).until(
        EC.url_contains("/web/index.php/attendance/")
    )
    wait_for_loader_to_disappear(driver)


def get_visible_submit_button(driver):
    buttons = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.CSS_SELECTOR, "button[type='submit']"))
    )

    for btn in buttons:
        if btn.is_displayed():
            return btn

    raise Exception("No visible submit button found")


def get_submit_text(driver):
    btn = get_visible_submit_button(driver)
    return btn.text.strip().lower()


def add_note(driver, text):
    wait_for_loader_to_disappear(driver)
    note_box = WebDriverWait(driver, 20).until(
        EC.presence_of_element_located((By.TAG_NAME, "textarea"))
    )
    note_box.clear()
    note_box.send_keys(text)


def set_date_by_typing(driver, xpath, value):
    for _ in range(5):
        try:
            wait_for_loader_to_disappear(driver)

            elem = WebDriverWait(driver, 20).until(
                EC.element_to_be_clickable((By.XPATH, xpath))
            )

            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elem)
            time.sleep(0.5)

            elem.click()
            time.sleep(0.3)
            elem.send_keys(Keys.CONTROL, "a")
            time.sleep(0.2)
            elem.send_keys(Keys.BACKSPACE)
            time.sleep(0.2)
            elem.send_keys(value)
            time.sleep(0.5)
            elem.send_keys(Keys.TAB)
            time.sleep(0.8)

            actual_value = driver.find_element(By.XPATH, xpath).get_attribute("value")
            print("Date field now:", actual_value)
            return actual_value == value

        except StaleElementReferenceException:
            time.sleep(1)

    return False


def set_time_by_js(driver, xpath, value):
    for _ in range(5):
        try:
            wait_for_loader_to_disappear(driver)

            elem = WebDriverWait(driver, 20).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )

            driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", elem)
            time.sleep(0.5)

            driver.execute_script("arguments[0].value = '';", elem)
            driver.execute_script("arguments[0].value = arguments[1];", elem, value)
            driver.execute_script("arguments[0].dispatchEvent(new Event('input', {bubbles: true}));", elem)
            driver.execute_script("arguments[0].dispatchEvent(new Event('change', {bubbles: true}));", elem)

            actual_value = driver.find_element(By.XPATH, xpath).get_attribute("value")
            print("Time field now:", actual_value)
            return actual_value == value

        except StaleElementReferenceException:
            time.sleep(1)

    return False


def set_punchout_datetime(driver):
    valid_punchout_date = "2026-04-06"
    valid_punchout_time = "09:00 PM"

    date_xpath = "//label[text()='Date']/../following-sibling::div//input"
    time_xpath = "//label[text()='Time']/../following-sibling::div//input"

    date_ok = set_date_by_typing(driver, date_xpath, valid_punchout_date)
    time_ok = set_time_by_js(driver, time_xpath, valid_punchout_time)

    actual_date = driver.find_element(By.XPATH, date_xpath).get_attribute("value")
    actual_time = driver.find_element(By.XPATH, time_xpath).get_attribute("value")

    print("Final punch out date:", actual_date)
    print("Final punch out time:", actual_time)

    if not date_ok:
        print("FAIL - Punch out date did not update correctly")
        return False

    if not time_ok:
        print("FAIL - Punch out time did not update correctly")
        return False

    return True


def force_click_submit(driver):
    wait_for_loader_to_disappear(driver)

    submit_btn = get_visible_submit_button(driver)
    driver.execute_script("arguments[0].scrollIntoView({block: 'center'});", submit_btn)
    time.sleep(1)

    try:
        submit_btn.click()
    except:
        driver.execute_script("arguments[0].click();", submit_btn)


def success_message_present(driver):
    possible_xpaths = [
        "//p[contains(@class,'oxd-text--toast-message')]",
        "//*[contains(text(),'Successfully')]",
        "//*[contains(text(),'Success')]"
    ]

    for xpath in possible_xpaths:
        try:
            el = WebDriverWait(driver, 3).until(
                EC.presence_of_element_located((By.XPATH, xpath))
            )
            if el.is_displayed():
                return el.text.strip()
        except TimeoutException:
            pass

    return ""


def valid_punchout_test(driver):
    go_to_punch_page(driver)

    current_url_before = driver.current_url
    button_text_before = get_submit_text(driver)

    print("Before punch out URL:", current_url_before)
    print("Before punch out button text:", button_text_before)

    if "out" not in button_text_before and "punchOut" not in current_url_before:
        print("SKIPPED - User is not currently in Punch Out state, so this test will not punch out")
        input("Press Enter to close the browser...")
        return

    if not set_punchout_datetime(driver):
        input("Press Enter to close the browser...")
        return

    add_note(driver, "Valid punch out test")
    force_click_submit(driver)

    time.sleep(5)

    success_msg = success_message_present(driver)
    current_url_after = driver.current_url
    button_text_after = get_submit_text(driver)

    print("After punch out URL:", current_url_after)
    print("After punch out button text:", button_text_after)

    if success_msg:
        print("PASS - Punch out successful")
        print("Success message:", success_msg)
    elif "in" in button_text_after or "punchIn" in current_url_after:
        print("PASS - Punch out successful, system returned to Punch In state")
   

    input("Press Enter to close the browser...")


if __name__ == "__main__":
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    driver.maximize_window()

    try:
        login_func(driver, username="Admin", pw="admin123")
        valid_punchout_test(driver)
    finally:
        driver.quit()