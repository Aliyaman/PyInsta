import imp
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from login_util import login
from time import sleep

full_url = "https://instagram.com/"

def like_all_posts(username, password, browser, accounts_name):
    accounts_name = full_url + accounts_name
    login(username, password, browser)
    sleep(5)
    browser.get(accounts_name)
    sleep(3)
    post_count = browser.find_element(By.CLASS_NAME, "g47SY").text
    post_count = int(post_count)
    act = ActionChains(browser)
    first_post = browser.find_element(By.CLASS_NAME, "v1Nh3.kIKUG._bz0w")
    first_post.click()
    for posts in range(int(post_count)):
        sleep(3)
        like_button = browser.find_element(By.CLASS_NAME, "fr66n")
        like_button.click()
        act.send_keys(Keys.ARROW_RIGHT).perform() 
    browser.quit()
