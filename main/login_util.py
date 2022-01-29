from selenium.webdriver.common.by import By
from time import sleep

url = "https://www.instagram.com/accounts/login/"
btn_xpath = "/html/body/div[1]/section/main/div/div/div/div/button"
btn_xpath2 = "/html/body/div[6]/div/div/div/div[3]/button[2]"

def login(username, password, browser):
    browser.get(url)
    sleep(3)
    username_input = browser.find_element(By.NAME, "username")
    password_input = browser.find_element(By.NAME, "password")
    login_button = browser.find_element(By.CLASS_NAME, "sqdOP.L3NKy.y3zKF")

    username_input.send_keys(username)
    password_input.send_keys(password)
    login_button.click()
    """
    sleep(8)
    not_now_button = driver.find_element(By.XPATH, btn_xpath)
    not_now_button.click()
    sleep(3)
    not_now_button2 = driver.find_element(By.XPATH, btn_xpath2)
    not_now_button2.click()
"""
