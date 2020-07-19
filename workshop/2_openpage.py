from selenium import webdriver
import time

# Get the path of the driver.
driver_path = "drivers/chromedriver.exe"
# Open chrome window
browser = webdriver.Chrome(driver_path)

# Open a page in browser window.
browser.get("https://codersarena.now.sh/")
# Prevent page from closing.
input()
browser.close()