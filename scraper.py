from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

site = "https://www.google.com/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.websitecarbon.com/")
time.sleep(10000)
driver.find_element_by_id('wgd-cc-url').send_keys(site)
driver.find_element_by_id('wgd-cc-url').click()