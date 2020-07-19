from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# setup browser
def setup():
    driver_path = "drivers/chromedriver.exe"
    return webdriver.Chrome(driver_path)


browser = setup()
browser.get('https://demoqa.com/automation-practice-form')
