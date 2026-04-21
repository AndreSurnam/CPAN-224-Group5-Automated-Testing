from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
# Made by Andre Tolentino

def login_func(driver, username, pw):
    driver.get("https://opensource-demo.orangehrmlive.com/")

    time.sleep(10)

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "username"))
    )

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.NAME, "password"))
    )

    user_nm = driver.find_element(By.NAME, "username")
    password = driver.find_element(By.NAME, "password")
    login_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit'")

    user_nm.clear()
    password.clear()

    user_nm.send_keys(username)
    password.send_keys(pw)
    login_btn.click()


if __name__ == "__main__":

    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    # Valid Login | TC_001
    # login_func(driver, username="admin", pw="admin123")
    # Invalid Login | TC_002
    login_func(driver, username="adnim", pw="123admin")

    print(driver.current_url)

    time.sleep(5)

    driver.close()
