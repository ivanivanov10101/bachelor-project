from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

site = "https://www.google.com/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.websitecarbon.com/")

driver.maximize_window()

driver.find_element_by_id('wgd-cc-url').send_keys(site)

time.sleep(5)

driver.find_element_by_id('js-new-test-button').click()

time.sleep(10000);