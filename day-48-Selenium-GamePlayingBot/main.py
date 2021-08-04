# from selenium import webdriver
#
# chrome_driver_path = "/Users/Eric/Documents/chromedriver_win32/chromedriver.exe"
# driver = webdriver.Chrome(executable_path=chrome_driver_path)
#
# #driver.get("https://www.amazon.com/Aroma-Housewares-Professional-Digital-Stainless/dp/B07Z8QR4W2?ref_=Oct_s9_apbd_omwf_hd_bw_bjv5Fj&pf_rd_r=WKGMQ3XH3DSKJS94Z467&pf_rd_p=8d23b16c-5b41-5135-aaec-bd1492730099&pf_rd_s=merchandised-search-10&pf_rd_t=BROWSE&pf_rd_i=678540011")
# #price = driver.find_element_by_id("priceblock_ourprice")
# #print(price.text)
#
# driver.get("https://python.org/")
# event_times = driver.find_elements_by_css_selector(".event-widget time")
# event_names = driver.find_elements_by_css_selector(".event-widget li a")
# events = {}
#
# for n in range(len(event_times)):
#     events[n] = {
#         "time": event_times[n].text,
#         "name": event_names[n].text,
#     }
# print(events)
#
# driver.close()
# #driver.quit()

from selenium import webdriver
import time

chrome_driver_path = "/Users/ericv/Documents/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(chrome_driver_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

# Get cookie to click on.
cookie = driver.find_element_by_id("cookie")

# Get upgrade item ids.
items = driver.find_elements_by_css_selector("#store div")
item_ids = [item.get_attribute("id") for item in items]

timeout = time.time() + 5
five_min = time.time() + 60 * 5  # 5minutes

while True:
    cookie.click()

    # Every 5 seconds:
    if time.time() > timeout:

        # Get all upgrade <b> tags
        all_prices = driver.find_elements_by_css_selector("#store b")
        item_prices = []

        # Convert <b> text into an integer price.
        for price in all_prices:
            element_text = price.text
            if element_text != "":
                cost = int(element_text.split("-")[1].strip().replace(",", ""))
                item_prices.append(cost)

        # Create dictionary of store items and prices
        cookie_upgrades = {}
        for n in range(len(item_prices)):
            cookie_upgrades[item_prices[n]] = item_ids[n]

        # Get current cookie count
        money_element = driver.find_element_by_id("money").text
        if "," in money_element:
            money_element = money_element.replace(",", "")
        cookie_count = int(money_element)

        # Find upgrades that we can currently afford
        affordable_upgrades = {}
        for cost, id in cookie_upgrades.items():
            if cookie_count > cost:
                affordable_upgrades[cost] = id

        # Purchase the most expensive affordable upgrade
        highest_price_affordable_upgrade = max(affordable_upgrades)
        print(highest_price_affordable_upgrade)
        to_purchase_id = affordable_upgrades[highest_price_affordable_upgrade]

        driver.find_element_by_id(to_purchase_id).click()

        # Add another 5 seconds until the next check
        timeout = time.time() + 5

    # After 5 minutes stop the bot and check the cookies per second count.
    if time.time() > five_min:
        cookie_per_s = driver.find_element_by_id("cps").text
        print(cookie_per_s)
        break