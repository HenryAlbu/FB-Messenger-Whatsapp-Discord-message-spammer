#!/usr/bin/env python3
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import platform 

# Variables
facebookEmail = "YOUR FACEBOOK EMAIL"
facebookPassword = "YOUR FACEBOOK PASSWORD"
friendName = "THE NAME OF THE PERSON THAT WILL GET THE MESSAGES"
sendDelay = 1;

if platform.system() == "Windows":
    driver = webdriver.Chrome('chromedriver.exe')
else:
    driver = webdriver.Chrome()

# Opens Facebook Messenger
driver.get('https://www.messenger.com/')
time.sleep(2.0)

# Login
driver.find_element_by_xpath('//*[@id="email"]').send_keys(facebookEmail)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys(facebookPassword)
driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

# Login via 2FA if need be
try:
    driver.find_element_by_xpath("//*[contains(text(), 'Continue')]").click()

    print("2FA required")
    tfa = str(input("Enter 2FA Code:"))
    
    driver.find_element_by_xpath('//*[@id="approvals_code"]').send_keys(tfa)
    driver.find_element_by_xpath("//*[contains(text(), 'Continue')]").click()
    driver.find_element_by_xpath("//*[contains(text(), 'Continue')]").click()
    driver.find_element_by_xpath("//*[contains(text(), 'Continue')]").click()
    driver.find_element_by_xpath("//*[contains(text(), 'This Was Me')]").click()
    driver.find_element_by_xpath("//*[contains(text(), 'Continue')]").click()

# No need to login via 2FA
except:
    print("2FA not required")

# Gets user from conversation list
getUser = driver.find_element_by_xpath("//*[contains(text(), '" + friendName + "')]").click()

# Reads Shrek script file and saves to movie_script list
movie_script = []
with open('script.txt', "r") as f:
    for line in f.readlines():
        for word in line.split():
            print(word)
            insertMessage = driver.find_element_by_class_name('_1mj')
            insertMessage.send_keys(word, Keys.ENTER)
            time.sleep(sendDelay)
