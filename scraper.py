from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

mobile_emulation = { "deviceName": "iPhone 12 Pro" }

chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get('https://sports.getfliff.com/')

time.sleep(10)  # Check the mobile view opens correctly

driver.quit()
