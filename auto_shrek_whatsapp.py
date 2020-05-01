#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import platform

# Variables
friendName = "Test"
sendDelay = 1
foundPage = 0

# Checks if on Mac or Windows
if platform.system() == "Windows":
    driver = webdriver.Chrome('chromedriver.exe')
else:
    driver = webdriver.Chrome()

# Opens Whatsapp
driver.get('https://web.whatsapp.com/')

# Waits for you to scan the whatsapp QR code
def page_load():
    getUser = driver.find_elements_by_xpath("//*[contains(text(), '" + friendName + "')]")
    if len(getUser) > 0:
        # waits 4 seconds to make sure page is loaded
        time.sleep(4)
        getUser[0].click()
        global foundPage
        foundPage = 1

while foundPage == 0:
    page_load()
    print("PLEASE SCAN QR CODE WITH PHONE")
    time.sleep(2)

# Reads Shrek script file and saves to movie_script list
movie_script = []
with open('script.txt', "r") as f:
    for line in f.readlines():
        for word in line.split():
            print(word)
            # Types words and submits
            actions = ActionChains(driver)
            actions.send_keys(word, Keys.ENTER)
            actions.perform()
            time.sleep(sendDelay)
