from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os
from dotenv import load_dotenv
import logging
import sys

def setup(logging):
    # logging.basicConfig(filename="workshop_driver.log",filemode="w" ,format='%(name)s - %(levelname)s - %(message)s')
    try:

        driver_path = "drivers/chromedriver.exe"
        return webdriver.Chrome(driver_path)
        
    except Exception as setup_ecx:
        logging.error("Driver Not Found. ERROR-"+str(setup_ecx))
        sys.exit(1)
    
def login(browser,user):
    # Open the linkedin login page
    browser.get("https://www.linkedin.com/login?fromSignIn=true&trk=guest_homepage-basic_nav-header-signin")

    # Elements
    email = browser.find_element_by_id("username")
    password = browser.find_element_by_id("password")
    signin = browser.find_element_by_class_name("btn__primary--large.from__button--floating")
    # Send keys
    email.send_keys(user['email'])
    password.send_keys(user['password'])
    time.sleep(1)
    signin.click()
    time.sleep(5)
    # CLick Submit
    # input("[+] Please solve the caaptcha.HIT enter when done.")

def add_note(browser):
    # elements
    try:
        add_note_btn = browser.find_element_by_class_name("artdeco-button__text")
    # Actions
        add_note_btn.click()
    except:
        return
    try:
        note_class_name = browser.find_element_by_id("custom-message")
        note_class_name.send_keys("Hello, Please add us to your professional linkedin network. Thanks !!!!")
        add_note_btn.click()
    except:
        return

def search(browser,search_term):

    # Elements
    search_bar = browser.find_element_by_class_name("search-global-typeahead__input.always-show-placeholder")

    # Actions
    search_bar.send_keys(search_term)
    search_bar.send_keys(Keys.ENTER)

    time.sleep(10)


    connect_btn_cn = "search-result__action-button.search-result__actions--primary.artdeco-button.artdeco-button--default.artdeco-button--2.artdeco-button--secondary"
    connect_btns = browser.find_elements_by_class_name(connect_btn_cn)

    for conn_btn in connect_btns:
        try:
            conn_btn.click()
            add_note(browser)
        except:
            pass


# Main

logging.basicConfig(filename="workshop.log",filemode="w" ,format='%(name)s - %(levelname)s - %(message)s')
browser = setup(logging)
browser.maximize_window()
load_dotenv()
user = {
    'email' : os.getenv("LINKEDIN_USERNAME"),
    'password' : os.getenv("LINKEDIN_PASSWORD"),
}
login(browser,user)
search(browser,"suraj kadam")