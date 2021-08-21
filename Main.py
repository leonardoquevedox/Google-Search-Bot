from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import time
import datetime
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.common import exceptions
from selenium.webdriver.common.keys import Keys
import os

# Initializes Gecko driver
driver = webdriver.Firefox()
links=["leopq", "leonardoquevedox", "pacleo"]

def handle_exception(e, message): 
    driver.quit()
    print(message)
    print(e)

def navigate_to_google():
    # Navigates into google main page
    driver.get('https://google.com')

def type_search_keyword():
    try:
        # --- Declares script variables
        search_term="Leonardo Quevedo"

        # --- Retrieves the search input
        search_input = driver.find_element_by_css_selector('input[type="text"]')
        print("✅ Found the search input...")

        # --- Types search term into the search input
        search_input.send_keys(search_term)
        print("✅ Filled it with the search term...")

        # --- Submits the search form
        search_input.send_keys(Keys.RETURN)
        print("✅ Submitted the search form.")

    except Exception as e:
        handle_exception(e, "💥 Whoops! There was an error executing the search step!")

def open_links_on_new_tabs():
    try:
        # --- Looks for link element
        link_element = driver.find_element_by_css_selector("a[href*=a]")

        # --- Retrieves URL from element
        link_url = link_element.get_attribute('href')
        print(link_url)

    except Exception as e:
        handle_exception(e, "💥 Whoops! There was an error executing the link opening step!")

def navigate_to_next_results_page():
    try:
        # --- Looks for link element
        link_elements = driver.find_elements_by_css_selector("a[href*=a]")

        for link in link_elements
            # --- Retrieves URL from element
            link_url = link_element.get_attribute('href')

            print(link_url)
        
        # --- Waits for 5 seconds
        time.sleep(5)
    except Exception as e:
        handle_exception(e, "💥 Whoops! There was an error executing the link opening step!")

def main():
    # --- Navigates into Google page
    navigate_to_google()
    # --- Types search keyword
    type_search_keyword()
    # --- Waits for 2 seconds
    time.sleep(2)
    # --- Open expected links
    open_links_on_new_tabs()
    # --- Waits for 2 seconds
    time.sleep(2)
    # --- Switch to next results page
    navigate_to_next_results_page()

main()