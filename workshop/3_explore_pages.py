from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# Get the path of the driver.
driver_path = "drivers/chromedriver.exe"
# Open chrome window
browser = webdriver.Chrome(driver_path)

# Open a page in browser window.
landing_page = browser.get("https://www.google.com/")

# Enter the search term
search_bar = browser.find_element_by_name("q")
search_bar.send_keys("Google")
search_bar.send_keys(Keys.ENTER)

# Prevent page from closing.
input()
browser.close()