from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from time import sleep
import settings
import platform

def start_spam():

    # Checks if on Mac or Windows
    print("Opening Chrome")
    if platform.system() == "Windows":
        driver = webdriver.Chrome('chromedriver.exe')
    else:
        driver = webdriver.Chrome()

    # Loggin into selected platform
    print("Starting Log in....")
    if settings.source == "Discord":
        # Opens Discord
        driver.get('https://discordapp.com/login')
        sleep(5)
        # Login
        driver.find_element_by_xpath('//*[@name="email"]').send_keys(settings.username_email)
        driver.find_element_by_xpath('//*[@name="password"]').send_keys(settings.password)
        driver.find_element_by_xpath('//*[@type="submit"]').click()

    elif settings.source == "Whatsapp":
        # Opens Whatsapp
        driver.get('https://web.whatsapp.com/')

        # Waits for you to scan the whatsapp QR code
        def page_load():
            get_users = driver.find_elements_by_xpath("//*[contains(text(), '" + settings.friend_name + "')]")
            if len(get_users) > 0:
                # waits 4 seconds to make sure page is loaded
                sleep(4)
                get_users[0].click()
                settings.found_page = 1

        while settings.found_page == 0:
            page_load()
            print("PLEASE SCAN QR CODE WITH PHONE")
            sleep(2)
    else:
        # Opens Facebook Messenger
        driver.get('https://www.messenger.com/')
        sleep(5)
        # Login
        driver.find_element_by_xpath('//*[@id="email"]').send_keys(settings.username_email)
        driver.find_element_by_xpath('//*[@id="pass"]').send_keys(settings.password)
        sleep(2)
        driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

    # Waits 8 seconds to finish loading page
    print("Waiting for a few seconds...")
    sleep(8)

    # Finds user in DM list
    if settings.source != "Whatsapp":
        driver.find_element_by_xpath("//*[contains(text(), '" + settings.friend_name + "')]").click()

    if settings.source == "Messenger":
        driver.refresh()
        sleep(5)

    # Starts message sending
    print("Starting messages...")
    with open(settings.script, "r") as f:
        for line in f.readlines():
            for i in range(settings.iterations):
                for word in line.split():
                    print("Sending: " + word)
                    # Types words and submits
                    actions = ActionChains(driver)
                    actions.send_keys(word, Keys.ENTER)
                    actions.perform()
                    sleep(float(settings.delay))
