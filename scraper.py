from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager
import time

mobile_emulation = {"deviceName": "iPhone 12 Pro"}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get('https://sports.getfliff.com/')
time.sleep(10)  # Wait for odds to load

# Select elements by their class
odds_elements = driver.find_elements(By.CLASS_NAME, "card-cell-label")

# Print odds to verify
for elem in odds_elements:
    print(elem.text)

driver.quit()