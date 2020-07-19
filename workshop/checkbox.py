from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# setup browser
def setup():
    driver_path = "drivers/chromedriver.exe"
    return webdriver.Chrome(driver_path)


def checkbox(browser):
    browser.get("https://demoqa.com/checkbox")
    checkbox = browser.find_element_by_class_name("rct-collapse.rct-collapse-btn")
    checkbox.click()
    # elements
    dropdown_list = browser.find_elements_by_class_name('rct-collapse.rct-collapse-btn')
    dropdown_list[2].click()
    inner_elements = browser.find_elements_by_class_name("rct-title")
    for inner_element in inner_elements:
        if inner_element.text == 'Office' :
            inner_element.click()
    
# Main
browser = setup()
checkbox(browser)

input()
browser.close()