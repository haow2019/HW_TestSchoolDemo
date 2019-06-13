# -*- coding:utf-8 -*-
from selenium import webdriver
from time import sleep
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def login(browserName, url):
    global driver
    try:
        # open_browser
        if browserName.lower() == "firefox":
            driver = webdriver.Firefox()
        elif browserName.lower() == "chrome":
            driver = webdriver.Chrome()
        else:
            driver = webdriver.Ie()

        # visit_url
        driver.get(url)

        # maximize_browser
        driver.maximize_window()
        # sleep
        sleep(3)

    except Exception as e:
        raise e
    # return driver
    return driver