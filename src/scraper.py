import os
import time  # For handling time-related functions
import re  # For regular expressions
import numpy as np  # For numerical operations
import pandas as pd  # For data manipulation and analysis
from bs4 import BeautifulSoup  # For web scraping
from selenium import webdriver  # For browser automation
from selenium.webdriver.chrome.service import Service  # For configuring the ChromeDriver service

def get_driver():
    """
    Creates a Chrome WebDriver instance for web scraping.
    :return: WebDriver -> configured instance of the Chrome WebDriver
    """

    my_service = Service(os.getenv('CHR_DRIVER'))  # setting the path to the ChromeDriver Executable
    my_options = webdriver.ChromeOptions()  # get the options for the ChromeDriver

    # Now, configure the ChromeDriver options
    my_options.add_argument('--ignore-certificate-errors')
    my_options.add_argument('--start-maximized')  # Start the browser in maximized mode

    # Creating a Chrome Web Driver instance with the specified service(executable) and options
    driver = webdriver.Chrome(service=my_service, options=my_options)

    return driver

def get_page_source(url, delay = 10):
    """
    Returns the page source, which is the parsed HTML content of the URL specified, making it ready to be scraped.
    :param url: url of the webpage to be scraped.
    :param delay: number of seconds to allow the webpage to load.
    :return: HTML parsed content of the URL returned as a BeuatifulSoup object
    """
    driver = get_driver()  # The get_driver() method we made in line 10
    driver.get(url)  # Open the specified URL in the browser
    time.sleep(delay)  # Introduce delay to allow time for the webpage to load

    # Get the page source by parsing using BeautifulSoup
    page_source = BeautifulSoup(driver.page_source, 'html.parser')
    driver.quit()  # Close the WebDriver
    return page_source  # Return the page source

def get_titles(page_source, first_page=False):
    """
    Extracts titles of the LeetCode problems from the given page source (HTML Object).
    :param page_source: HTML Object of page to extract from.
    :param first_page: (optional) Flag indicator if it's the first page. Default is False
    :return: list of titles
    """
    # start_index's value depends on whether the page_source is of the first page or not.
    # This is because, the first page has the 'Problem Of The Day' in the table which we do not need.
    # The rest of the pages of the problem set pages do not have the 'Problem Of The Day'.
    start_index = 1 if first_page else 0

    

