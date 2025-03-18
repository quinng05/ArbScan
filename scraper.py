from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import time

mobile_emulation = {"deviceName": "iPhone 12 Pro"}
chrome_options = webdriver.ChromeOptions()
chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
driver.get('https://sports.getfliff.com/')

try:
    # Wait until elements with class 'card-cell-label' are present
    WebDriverWait(driver, 15).until(
        EC.presence_of_all_elements_located((By.CLASS_NAME, "card-cell-label"))
    )
    odds_elements = driver.find_elements(By.CLASS_NAME, "card-cell-label")

    for elem in odds_elements:
        print(elem.text)

finally:
    driver.quit()