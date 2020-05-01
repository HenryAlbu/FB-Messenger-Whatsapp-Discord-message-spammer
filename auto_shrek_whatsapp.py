#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import platform 


# Variables
friendName = "THE NAME OF THE PERSON THAT WILL GET THE MESSAGES"
sendDelay = 1
foundPage = 0

# Opens Whatsapp
dif platform.system() == "Windows":
    driver = webdriver.Chrome('chromedriver.exe')
else:
    driver = webdriver.Chrome()
    
driver.get('https://web.whatsapp.com/')

# Waits for you to scan the whatsapp QR code
def page_load():
    getUser = driver.find_elements_by_xpath("//*[contains(text(), '" + friendName + "')]")
    if len(getUser) > 0:
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
            insertMessage = driver.find_element_by_xpath('//*[@id="main"]/footer/div[1]/div[2]/div/div[2]')
            insertMessage.send_keys(word, Keys.ENTER)
            time.sleep(sendDelay)
