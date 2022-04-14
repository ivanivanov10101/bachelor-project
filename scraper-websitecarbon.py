from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

import time

site = "https://www.google.com/"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get("https://www.websitecarbon.com/")

driver.maximize_window()

driver.find_element(By.ID, 'wgd-cc-url').send_keys(site)

time.sleep(1)

driver.find_element(By.ID, 'js-new-test-button').click()

driver.implicitly_wait(6)

text = driver.find_element(By.CLASS_NAME, "js-countup-content").text
print(text)
time.sleep(10000);