from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
driver.get('https://play.getfliff.com/')

time.sleep(10)  # Keeps the browser open for 10 seconds

driver.quit()

