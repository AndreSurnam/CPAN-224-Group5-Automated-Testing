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

    ############################################################################################################
    # Only necessary if testing in standard view (width is less than half of the screen)

    # WebDriverWait(driver, 10).until(
    #     EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[3]/button"))
    # )

    # dropdown_button = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[1]/div[2]/div[3]/button")
    # dropdown_button.click()

    ############################################################################################################

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]"))
    )

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]"))
    )

    WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]"))
    )

    user_role = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[1]/div/div[2]/div/div[2]/div/div/div[1]")
    search_btn = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[2]")
    reset_btn = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[1]/div[2]/form/div[2]/button[1]")

    user_role.click()
    time.sleep(sleep_timer)

    ess_option = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.XPATH, "//span[text()='ESS']"))
    )

    ess_option.click()
    time.sleep(sleep_timer)

    search_btn.click()
    time.sleep(3)

    reset_btn.click()
    time.sleep(5)

if __name__ == "__main__":

    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    erase_full_name(driver)
    print(driver.current_url)

    time.sleep(5)

    driver.close()