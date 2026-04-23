# Made by: Tyler Ly
# Humber ID: n01725055

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
import time
from login import login_func

sleep_timer = 0.5

def delete_info(field):
    time.sleep(sleep_timer)
    field.click()
    time.sleep(sleep_timer)
    field.send_keys(Keys.CONTROL + "a")
    time.sleep(sleep_timer)
    field.send_keys(Keys.DELETE)
    time.sleep(sleep_timer)

def erase_full_name(driver):
    login_func(driver, "admin", "admin123")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a"))
    )

    my_info = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a")
    my_info.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[1]/div[2]/input"))
    )

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[2]/div[2]/input"))
    )

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div/div/div[2]/div[3]/div[2]/input"))
    )

    first_name = driver.find_element(By.NAME, "firstName")
    middle_name = driver.find_element(By.NAME, "middleName")
    last_name = driver.find_element(By.NAME, "lastName")

    save_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    delete_info(first_name)
    delete_info(middle_name)
    delete_info(last_name)

    save_btn.click()
    time.sleep(sleep_timer)
    save_btn.click()
    time.sleep(sleep_timer)
    save_btn.click()
    time.sleep(sleep_timer)


if __name__ == "__main__":

    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    erase_full_name(driver)
    print(driver.current_url)

    time.sleep(5)

    driver.close()