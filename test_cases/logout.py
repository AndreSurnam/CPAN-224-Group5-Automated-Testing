from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login import login_func
import time
# Made by Andre Tolentino

def logout_func(driver):
    login_func(driver, username="admin", pw="admin123")

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/img"))
    )

    profile = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[3]/ul/li/span/img")
    profile.click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a"))
    )

    logout_btn = driver.find_element(By.XPATH, "/html/body/div/div[1]/div[1]/header/div[1]/div[3]/ul/li/ul/li[4]/a")
    logout_btn.click()


if __name__ == "__main__":

    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    # Logout | TC_003
    logout_func(driver)
    print(driver.current_url)

    time.sleep(5)

    driver.close()
