from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time
import platform


# Variables
sendDelay = 1
email = "YOUR DISCORD EMAIL"
password = "YOUR DISCORD PASSWORD"
friendName = "THE NAME OF THE PERSON THAT WILL GET THE MESSAGES"

# Checks if on Mac or Windows
if platform.system() == "Windows":
    driver = webdriver.Chrome('chromedriver.exe')
else:
    driver = webdriver.Chrome()

# Opens Discord
driver.get('https://discordapp.com/login')

# Login
driver.find_element_by_xpath('//*[@name="email"]').send_keys(email)
driver.find_element_by_xpath('//*[@name="password"]').send_keys(password)
driver.find_element_by_xpath('//*[@type="submit"]').click()

# Waits 8 seconds to finish loading page
time.sleep(8)

# Finds user in DM list
getUser = driver.find_element_by_xpath("//*[contains(text(), '" + friendName + "')]").click()

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
