from lib2to3.pgen2 import driver
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from login_util import login
from time import sleep

url = "https://instagram.com/"
#driver = webdriver.Firefox()
#driver.set_window_size(800,600)
login_url = "https://www.instagram.com/accounts/login/"
btn_xpath = "/html/body/div[1]/section/main/div/div/div/div/button"
btn_xpath2 = "/html/body/div[6]/div/div/div/div[3]/button[2]"
follow_button_xpth = "/html/body/div[1]/section/main/div/header/section/div[1]/div[2]/div/div/a/button"


def follow_accounts(username, password, accounts_list, browser):
    login(username, password, browser)
    sleep(5)
    for users in accounts_list:
        full_link = url + users
        browser.get(full_link) 
        sleep(3)
        try:
            browser.find_element(By.CLASS_NAME, "_7UhW9.x-6xq.qyrsm.KV-D4.uL8Hv.l4b0S")
            print(f"There is no account {users}. Please control name.")
        except NoSuchElementException:
            try:
                follow_button = browser.find_element(By.CLASS_NAME, "_5f5mN.jIbKX._6VtSN.yZn4P")
                follow_button.click()
                sleep(2.5)
            except NoSuchElementException as exception:
                follow_button = browser.find_element(By.CLASS_NAME, "sqdOP.L3NKy.y3zKF")
                follow_button.click()
                sleep(2.5)

    print(f"{len(accounts_list)} users followed!") 
    browser.quit()
