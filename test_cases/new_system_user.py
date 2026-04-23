from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from login import login_func

sleep_timer = 0.5

def insert_info(field, s):
    time.sleep(sleep_timer)
    field.click()
    time.sleep(sleep_timer)
    field.send_keys(s)
    time.sleep(sleep_timer)

def erase_full_name(driver):
    login_func(driver, "admin", "admin123")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a"))
    )

    admin = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[1]/a")
    admin.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button"))
    )

    add_btn = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button")

    time.sleep(sleep_timer)
    add_btn.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]"))
    )

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input"))
    )

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]"))
    )

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input"))
    )

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input"))
    )

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input"))
    )

    user_role = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[1]/div/div[2]/div/div/div[1]")
    employee_name = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[2]/div/div[2]/div/div/input")
    status = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[3]/div/div[2]/div/div/div[1]")
    user_name = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[1]/div/div[4]/div/div[2]/input")
    password = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[1]/div/div[2]/input")
    confirm_password = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[2]/div/div[2]/div/div[2]/input")

    save_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    # User Role
    user_role.click()
    time.sleep(sleep_timer)

    ess_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='ESS']"))
    )

    ess_option.click()
    time.sleep(sleep_timer)

    # Employee Name
    insert_info(employee_name, "Thomas")

    thomas_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Thomas Kutty Benny']"))
    )

    thomas_option.click()
    time.sleep(sleep_timer)

    # Status
    status.click()
    time.sleep(sleep_timer)

    enabled_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='Enabled']"))
    )

    enabled_option.click()
    time.sleep(sleep_timer)

    insert_info(user_name, "Thomas Kutty Benny") # User Name
    insert_info(password, "password123$") # Password
    insert_info(confirm_password, "password123$") # Confirm Password

    save_btn.click()
    time.sleep(sleep_timer)

if __name__ == "__main__":

    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    erase_full_name(driver)
    print(driver.current_url)

    time.sleep(5)

    driver.close()