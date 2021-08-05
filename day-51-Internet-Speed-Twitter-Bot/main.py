import os
from selenium import webdriver
import time
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

PROMISED_DOWN = 75
PROMISED_UP = 75
CHROME_DRIVER_PATH = "/Users/ericv/Documents/chromedriver_win32/chromedriver.exe"
TWITTER_EMAIL = os.environ["TWITTER_EMAIL"]
TWITTER_PASSWORD = os.environ["TWITTER_PASSWORD"]

class InternetSpeedTwitterBot:
    def __init__(self, driver_path):
        self.driver = webdriver.Chrome(executable_path=driver_path)
        self.up = 0
        self.down = 0

    def get_internet_speed(self):
        self.driver.get("https://www.speedtest.net/")
        self.driver.maximize_window()
        # Depending on your location, you might need to accept the GDPR pop-up.
        # accept_button = self.driver.find_element_by_id("_evidon-banner-acceptbutton")
        # accept_button.click()
        time.sleep(2)
        go_button = self.driver.find_element_by_css_selector(".start-button a")
        go_button.click()

        time.sleep(60)
        self.up = self.driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[3]/div/div[2]/span").text
        self.down = self.driver.find_element_by_xpath("//*[@id='container']/div/div[3]/div/div/div/div[2]/div[3]/div[3]/div/div[3]/div/div/div[2]/div[1]/div[2]/div/div[2]/span").text

        print(self.up)
        print("test")
        print(self.down)
    def tweet_at_provider(self):
        self.driver.get("https://twitter.com/login")
        time.sleep(2)
        self.driver.maximize_window()
        username_textbox = self.driver.find_element_by_xpath("/html/body/div/div/div/div[2]/main/div/div/div[2]/form/div/div[1]/label/div/div[2]/div/input")
        username_textbox.send_keys(TWITTER_EMAIL)
        password_textbox = self.driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[2]/label/div/div[2]/div/input")
        password_textbox.send_keys(TWITTER_PASSWORD)
        submit_login_button = self.driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div[2]/form/div/div[3]/div/div")
        submit_login_button.click()

        time.sleep(2)
        #tweet = "hi"
        tweet = f"Hey Internet Provider, why is my internet speed {self.down}down/{self.up}up when I pay for {PROMISED_DOWN}down/{PROMISED_UP}up?"
        tweet_textbox = self.driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[1]/div/div/div/div/div/div/div/div/div/div[1]/div/div/div/div[2]/div/div/div/div")
        tweet_textbox.send_keys(tweet)
        tweet_submit_button = self.driver.find_element_by_xpath("//*[@id='react-root']/div/div/div[2]/main/div/div/div/div[1]/div/div[2]/div/div[2]/div[1]/div/div/div/div[2]/div[4]/div/div/div[2]/div[3]/div/span/span")
        tweet_submit_button.click()

bot = InternetSpeedTwitterBot(CHROME_DRIVER_PATH)
bot.get_internet_speed()
bot.tweet_at_provider()

