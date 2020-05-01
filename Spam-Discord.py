from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

#variables
sendDelay = 1
email = 'ENTER EMAIL'
password = 'ENTER PASSWORD'
#if sending as pm, insert as "@PM_NAME"
chatdm = 'ENTER CHAT NAME'
#directory var of chromedriver
directory = 'C:\\DIRECTORY\chromedriver.exe'


#creates new object browser
browser = webdriver.Chrome(directory)

#opens new browser w/discordapp
browser.get('https://discordapp.com')

#presses log-in button
browser.find_element_by_xpath('//*[@id="app-mount"]/div/div/div/header[1]/nav/ul[2]/li[4]/a').click()

#logs in with info details
browser.find_element_by_xpath('//*[@name="email"]').send_keys(email)
browser.find_element_by_xpath('//*[@name="password"]').send_keys(password)
browser.find_element_by_xpath('//*[@type="submit"]').click()

#waits 8 seconds to load
time.sleep(8)

#INSERT LINK OF PM CHANNEL OR SERVER TO SPAM
browser.get('https://discordapp.com/INPUTLINK')

#delay 3 seconds
time.sleep(3)
movie_script = []
with open('script.txt', "r") as f:
    for line in f.readlines():
        for word in line.split():
            print(word)
            insertMessage = browser.find_element_by_xpath(f'//*[@aria-label="Message {chatdm}"]')
            insertMessage.send_keys(word, Keys.ENTER)
            time.sleep(sendDelay)