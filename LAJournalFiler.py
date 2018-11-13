# File management
import os
import json
import glob

# Web control
from selenium import webdriver
from selenium.common.exceptions import WebDriverException
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

def setup_driver_and_instance():
    global driver

    driver = webdriver.Chrome()

    driver.get(("https://edelivery.lasc.journaltech.com/public-portal/"))
