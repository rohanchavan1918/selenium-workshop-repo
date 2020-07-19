from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# setup browser
def setup():
    driver_path = "drivers/chromedriver.exe"
    return webdriver.Chrome(driver_path)


def textbox(browser):
    browser.maximize_window()
    browser.get("https://demoqa.com/text-box")
    # elements
    full_name = browser.find_element_by_id("userName")
    email = browser.find_element_by_id("userEmail")
    current_address = browser.find_element_by_id("currentAddress")
    perm_address =  browser.find_element_by_id("permanentAddress")
    btn = browser.find_element_by_id('submit')

    # send keys
    full_name.send_keys("some keys")
    email.send_keys("baburao@gmail.com")
    current_address.send_keys("some keys")
    perm_address.send_keys("some keys")
    
    btn.click()

    input()

# Main
browser = setup()
textbox(browser)

browser.close()