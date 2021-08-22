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
driver.implicitly_wait(5) # seconds
keywords=["leopq", "leonardoquevedox", "pacleo"]
result_pages=["1", "2", "3", "4", "5", "6", "7", "8", "9", "10"]

def handle_exception(e, message): 
    # driver.quit()
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
        # --- Retrieves main tab from driver
        main_tab = driver.current_window_handle
        for keyword in keywords: 
            # --- Looks for link elements
            keyword_links = driver.find_elements_by_css_selector("a[href*={}]".format(keyword))
            # --- Transform them into URLs
            link_urls = [link.get_attribute('href') for link in keyword_links]
            # print(link_urls)

            # --- For every link URL, do
            for link_url in link_urls:
                print("\n")
                print("✅ Found link: ", link_url)
                driver.execute_script("window.open('{}','_blank')".format(link_url))
                
        # --- Switches back to main tab
        driver.switch_to_window(main_tab)

    except Exception as e:
        handle_exception(e, "💥 Whoops! There was an error executing the link opening step!")

def navigate_to_next_results_page():
    try:
        # --- Clicks the next page link
        driver.execute_script("arguments[0].click();", driver.find_element_by_css_selector("#pnnext"))
        print("✅ Clicked the next page link")

    except Exception as e:
        print("✅ Navigated to next page")
        # handle_exception(e, "💥 Whoops! There was an error executing the navgation to next page step!")

def main():
    # --- Navigates into Google page
    navigate_to_google()
    # --- Types search keyword
    type_search_keyword()
    # --- Waits for 2 seconds
    time.sleep(2)

    # For every result page, do:
    for result_page in result_pages:
        # --- Open expected links
        open_links_on_new_tabs()
        # --- Switch to next results page
        navigate_to_next_results_page()
        # --- Prints separator line
        # print("\n")

main()