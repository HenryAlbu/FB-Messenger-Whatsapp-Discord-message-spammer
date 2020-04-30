from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Variables
facebookEmail = "YOUR FACEBOOK EMAIL"
facebookPassword = "YOUR FACEBOOK PASSWORD"
friendName = "THE NAME OF THE PERSON THAT WILL GET THE MESSAGES"
sendDelay = 1;

# Opens Facebook Messenger
driver = webdriver.Chrome('chromedriver.exe')
driver.get('https://www.messenger.com/')

# Login
driver.find_element_by_xpath('//*[@id="email"]').send_keys(facebookEmail)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys(facebookPassword)
driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

# Gets user from conversation list
getUser = driver.find_element_by_xpath("//*[contains(text(), '" + friendName + "')]").click()

# Reads Shrek script file and saves to movie_script list
movie_script = []
with open('script.txt', "r") as f:
    movie_script = f.read().split()

# printing the list using loop
for x in range(len(movie_script)):
    print(movie_script[x])
    insertMessage = driver.find_element_by_class_name('_1mj')
    insertMessage.send_keys(movie_script[x], Keys.ENTER)
    time.sleep(sendDelay)







