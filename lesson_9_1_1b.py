from selenium import webdriver
from selenium.webdriver.support.color import Color
from selenium.webdriver.support.select import Select

# imports for selenium WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By

# imports form internal modules
from browser import Browser
from UIElement import UIElement as Element

import time

# Exercise #1
#
# Into existing tests:
# - add a Browser object to the tests where you still have Selenium webdriver initialization
# - update code of lines for WebDriverWait to use the new method from the Browser class - get_wd_wait
# - update code to use new class UIElement in places instead of find_element_by*

# May 14th, 2021
# student Evgeny Abdulin

browser = Browser("https://techskillacademy.net/brainbucket/index.php?route=account/login", "Firefox")
driver = browser.get_driver()

# going to Registration form
account_link = browser.get_wd_wait().\
    until(ec.element_to_be_clickable((By.XPATH, "//span[contains(.,'My Account')]"))).click()
register_link = browser.get_wd_wait().\
    until(ec.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Register')]"))).click()
# checking if title Register Account is visible
register_title = browser.get_wd_wait().until(ec.visibility_of_element_located((By.XPATH, "//h1")))

# back to Home page with some delay to be able to see what was done on the page
time.sleep(2)
driver.back()

# going to Login form
account_link = browser.get_wd_wait().\
    until(ec.element_to_be_clickable((By.XPATH, "//span[contains(.,'My Account')]"))).click()
login_link = browser.get_wd_wait().\
    until(ec.element_to_be_clickable((By.XPATH, "//a[contains(text(),'Login')]"))).click()
# checking if title Register Account is visible
login_title = browser.get_wd_wait().\
    until(ec.visibility_of_element_located((By.XPATH, "//h2[contains(text(),'Returning Customer')]")))

# add some sleep time to be able to see the result
time.sleep(5)

browser.shutdown()
