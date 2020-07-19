from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

# setup browser
def setup():
    driver_path = "drivers/chromedriver.exe"
    return webdriver.Chrome(driver_path)


def search(browser,search_term):
    searchbox = browser.find_element_by_id("searchBox")
    # Clear the searhc filed
    searchbox.send_keys(Keys.CONTROL,'a')
    searchbox.send_keys(Keys.DELETE)
    searchbox.send_keys(search_term)
    # add on click button
    searchbtn = browser.find_element_by_id("basic-addon2")
    searchbtn.click()

# MAIN
browser = setup()
browser.get("https://demoqa.com/books")
# while True:
#     user_ip = input("Search y/n")
#     if user_ip == 'y' or user_ip == 'n':
#         if user_ip == 'y':
#             search_term = input("ENter the search term")
#             search(browser,search_term)
#             time.sleep(2)
#         else:
#             break
#     else:
#         print("Invalid input")

search_terms = ["python","javascript","c"]
for search_term in search_terms:
    search(browser,search_term)
    time.sleep(2)
browser.close()