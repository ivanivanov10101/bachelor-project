from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By

import time

def start():
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    driver.get("https://www.google.com")
    driver.maximize_window()
    return driver

def scrape(driver, site):
    driver.get(site)
    driver.find_element(By.ID, 'wgd-cc-url').send_keys(site)

    time.sleep(1)

    driver.find_element(By.ID, 'js-new-test-button').click()

    time.sleep(6)

    text = driver.find_element(By.XPATH, "/html/body/div/main/article/div[1]/div/div[2]/p/span/span/span").text
    time.sleep(1)
    driver.execute_script("window.scrollBy(0,500)","")
    time.sleep(1)
    co2 = driver.find_element(By.XPATH, "/html/body/div/main/article/div[2]/div[2]/p/span/span/span").text
    time.sleep(1)

    energy = driver.find_element(By.XPATH, "/html/body/div/main/article/div[3]/div[2]/p/span").text

    driver.execute_script("window.scrollBy(0,1000)","")
    time.sleep(1)
    co2equiv = driver.find_element(By.XPATH, "/html/body/div/main/article/div[4]/div[1]/div[2]/div/h4/span[1]").text

    print(text)
    print("___")
    print(co2)
    print("___")
    print(energy)
    print("___")
    print(co2equiv)
    time.sleep(10000);

start()
import csv
with open('db.csv', newline='') as csvfile:
    spamreader = csv.reader(csvfile, delimiter=',', quotechar='|')
    for row in spamreader:
        scrape(row[1])


