from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome_path = "C:/Development/chromedriver.exe"
driver = webdriver.Chrome(executable_path= chrome_path)
driver.get("http://orteil.dashnet.org/experiments/cookie/")

pause= time.time() + 5
five_min = time.time() + 60*5 # 5minutes



game_is_on = True
cookie = driver.find_element_by_id("cookie")

while game_is_on:
    cookie.click()

    if time.time() > pause:
        all_values = driver.find_elements_by_css_selector("#store b")
        prices = []

        for value in all_values:
            price = value.text
            if price != "":
                prices.append(int(price.split("-")[1].replace(",", "")))

        money = driver.find_element_by_id("money").text
        affordable_updates = []
        for price in prices:
            if int(money) >= price:
                affordable_updates.append(price)


        update = 0
        for n in range(-1, len(affordable_updates) -1):
            if affordable_updates[n] >= update:
                update = affordable_updates[n]
        if update != 0:
            index_value = prices.index(update)
            all_values[index_value].click()







