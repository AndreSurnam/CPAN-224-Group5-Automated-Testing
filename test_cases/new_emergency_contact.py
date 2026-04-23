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
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a"))
    )

    my_info = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/aside/nav/div[2]/ul/li[6]/a")
    my_info.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/a"))
    )

    emergency_contacts = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[1]/div[2]/div[3]/a")

    time.sleep(sleep_timer)
    emergency_contacts.click()

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button"))
    )

    add_btn = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/div/button")

    time.sleep(sleep_timer)
    add_btn.click()

    name = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[1]/div/div[2]/input")
    relationship = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[1]/div/div[2]/div/div[2]/input")
    telephone = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[1]/div/div[2]/input")
    mobile = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[2]/div/div[2]/input")
    work_telephone = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/div/div[2]/div[1]/form/div[2]/div/div[3]/div/div[2]/input")

    save_btn = driver.find_element(By.CSS_SELECTOR, "button[type='submit']")

    insert_info(name, "Tyler")
    insert_info(relationship, "Cousin")
    insert_info(telephone, "2889-555-9012")
    insert_info(mobile, "612-746-2934")
    insert_info(work_telephone, "1234567890")

    save_btn.click()
    time.sleep(sleep_timer)

if __name__ == "__main__":

    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    erase_full_name(driver)
    print(driver.current_url)

    time.sleep(5)

    driver.close()