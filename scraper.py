from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

def scrape_fliff_odds():
    mobile_emulation = {"deviceName": "iPhone 12 Pro"}
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)

    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=chrome_options)
    driver.get('https://sports.getfliff.com/')

    odds_data = []

    try:
        WebDriverWait(driver, 15).until(        # Wait for page to load, or until time out (15 sec)
            EC.presence_of_all_elements_located((By.CLASS_NAME, "card-cell-label"))
        )

        odds_elements = driver.find_elements(By.CLASS_NAME, "card-cell-label")      # Find odds

        for elem in odds_elements:
            odds_value = elem.text.strip()

            try:
                container = elem.find_element(By.XPATH, './ancestor::div[contains(@class, "card-shared-container")]')
                event_name_element = container.find_element(By.CLASS_NAME, 'card-note__title')
                event_name = event_name_element.text.strip()
            except:
                event_name = "Unknown Event"  # fallback in case something breaks

            odds_data.append({
                "platform": "Fliff",
                "event_name": event_name,
                "team_or_outcome": "",   
                "odds_value": odds_value,
                "odds_type": "moneyline",
            })

    finally:
        driver.quit()

    return odds_data