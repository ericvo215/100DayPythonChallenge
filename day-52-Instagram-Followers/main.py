import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException, ElementClickInterceptedException

CHROME_DRIVER_PATH = "/Users/ericv/Documents/chromedriver_win32/chromedriver.exe"
SIMILAR_ACCOUNT = "tomholland"
USERNAME = os.environ["USERNAME"]
PASSWORD = os.environ["PASSWORD"]

class InstaFollower:

    def __init__(self, path):
        self.driver = webdriver.Chrome(executable_path=path)

    def login(self):
        self.driver.get("https://www.instagram.com/accounts/login/")
        self.driver.maximize_window()
        time.sleep(1.5)
        username_textbox = self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[1]/div/label/input")
        username_textbox.send_keys(USERNAME)
        password_textbox = self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[2]/div/label/input")
        password_textbox.send_keys(PASSWORD)
        login_button = self.driver.find_element_by_xpath("//*[@id='loginForm']/div/div[3]")
        login_button.click()
        time.sleep(4)
        not_now = self.driver.find_element_by_xpath("/html/body/div[5]/div/div/div/div[3]/button[2]")
        not_now.click()
        time.sleep(2)


    def find_followers(self):
        search_textbox = self.driver.find_element_by_xpath("//*[@id='react-root']/section/nav/div[2]/div/div/div[2]/input")
        search_textbox.send_keys(SIMILAR_ACCOUNT)
        time.sleep(2)
        search_textbox.send_keys(Keys.RETURN)
        search_textbox.send_keys(Keys.RETURN)
        time.sleep(2)

        followers = self.driver.find_element_by_xpath("//*[@id='react-root']/section/main/div/header/section/ul/li[2]/a")
        followers.click()
        time.sleep(2)

    def follow(self):
        all_buttons = self.driver.find_elements_by_css_selector("li button")
        for button in all_buttons:
            try:
                button.click()
                time.sleep(1)
            except ElementClickInterceptedException:
                cancel_button = self.driver.find_element_by_xpath('/html/body/div[5]/div/div/div/div[3]/button[2]')
                cancel_button.click()


bot = InstaFollower(CHROME_DRIVER_PATH)
bot.login()
bot.find_followers()
bot.follow()