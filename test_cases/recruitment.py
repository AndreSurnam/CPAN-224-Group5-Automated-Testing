from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from login import login_func
import time
# Made by Andre Tolentino


def add_candidate(driver, first_name, last_name, email_adr):
    login_func(driver, username="admin", pw="admin123")

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.LINK_TEXT, "Recruitment"))
    )

    recruitment_link = driver.find_element(By.LINK_TEXT, "Recruitment")
    recruitment_link.click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located(
            (By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button"))
    )

    add_btn = driver.find_element(
        By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div[2]/div[1]/button")
    add_btn.click()

    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.NAME, "firstName"))
    )

    first_nm = driver.find_element(By.NAME, "firstName")
    last_nm = driver.find_element(By.NAME, "lastName")
    email = driver.find_element(
        By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[3]/div/div[1]/div/div[2]/input")

    first_nm.clear()
    last_nm.clear()
    email.clear()

    first_nm.send_keys(first_name)
    last_nm.send_keys(last_name)
    email.send_keys(email_adr)

    save_btn = driver.find_element(
        By.XPATH, "/html/body/div/div[1]/div[2]/div[2]/div/div/form/div[8]/button[2]")
    save_btn.click()


if __name__ == "__main__":
    service = Service(executable_path="chromedriver.exe")
    driver = webdriver.Chrome(service=service)

    # Succesful Add Candidate | TC_004
    # add_candidate(driver, first_name="John", last_name="Doe", email_adr="john.doe@gmail.com")
    # Unsuccesful Add Candidate | TC_005
    add_candidate(driver, first_name="", last_name="", email_adr="")

    print(driver.current_url)

    time.sleep(15)

    driver.close()
