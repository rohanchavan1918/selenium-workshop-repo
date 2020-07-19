# THESE ARE SECRET CODES, DONOT SHARE.

from selenium import webdriver

# Get the path of the driver.
driver_path = "drivers/chromedriver.exe"

# Open chrome window
browser = webdriver.Chrome(driver_path)
browser.close()
