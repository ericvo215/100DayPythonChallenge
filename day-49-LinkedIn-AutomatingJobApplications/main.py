from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

import os
import time

from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

LINKEDIN_USERNAME = os.environ["LINKEDIN_USERNAME"]
LINKEDIN_PASSWORD = os.environ["LINKEDIN_PASSWORD"]

chrome_driver_path = "/Users/ericv/Documents/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)

driver.get("https://www.linkedin.com/")
driver.maximize_window()
#LOGIN
username_field = driver.find_element_by_name("session_key")
username_field.send_keys(LINKEDIN_USERNAME)

username_field = driver.find_element_by_name("session_password")
username_field.send_keys(LINKEDIN_PASSWORD)

submit_button = driver.find_element_by_css_selector(".sign-in-form__submit-button")
submit_button.click()
time.sleep(2)

#Declining saving browser session. May need to be commented
# browser_session_not_now_button = driver.find_element_by_css_selector(".btn__secondary--large-muted")
# browser_session_not_now_button.click()

#Declining add phone for security. May need to be commented
# phone_not_now = driver.find_element_by_css_selector(".secondary-action")
# phone_not_now.click()

#Clicks on job button
jobs_button = driver.find_element_by_link_text("Jobs")
jobs_button.click()
time.sleep(2)

#Search for jobs in textbox
jobs_searchbox = driver.find_element_by_css_selector(".jobs-search-box--large .jobs-search-box__inner input")
jobs_searchbox.send_keys("python")
jobs_searchbox.send_keys(Keys.ENTER)
time.sleep(2)

all_listings = driver.find_elements_by_css_selector(".job-card-container--clickable")
#print(all_listings.count())
for listing in all_listings:
    print("called")
    listing.click()
    print("hi")
    time.sleep(1)
    #add Saved below here
    try:
        # save_button = driver.find_elements_by_css_selector(".artdeco-button--2")
        # save_button.click()
        print("hi")
        time.sleep(1)
    except NoSuchElementException:
        print("No application button, skipped.")
        continue
    time.sleep(1)

    # try:
    #     apply_button = driver.find_element_by_css_selector(".artdeco-button--secondary")
    #     apply_button.click()
    #     time.sleep(3)
    # except NoSuchElementException:
    #     print("No application button, skipped.")
    #     continue
#Search Jobs
#search_jobs = driver.find_elements_by_xpath("//*[@id='ember26']/input")
#print(search_jobs.text)
#search = WebDriverWait(driver, 10).until(
    #expected_conditions.presence_of_element_located((By.XPATH, "//input[@placeholder='Search']"))).click()
#search_jobs.click()
#search_jobs.send_keys("python")
#search_jobs.send_keys(Keys.ENTER)






#login_button.click()
print(driver.current_url)





#input__input
#username
#current-password