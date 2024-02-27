from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 18
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(4)
    
    try:
        driver.find_element(By.CSS_SELECTOR, 'button#cookie-accept').click()
    except Exception as e:
        print(f'Scraper{key} cookiee button: {e}')
        
    time.sleep(4)
    
    items = driver.find_elements(By.CSS_SELECTOR, 'tr.data-row')
    
    data = []
    
    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()
        location = item.find_element(By.CSS_SELECTOR, "td.colLocation").text.strip()
        
        if location.split(',')[-2].strip() in ["US", "UK"]:
            data.append([
                item.find_element(By.CSS_SELECTOR, "a").text.strip(),
                com,
                location,
                link
            ])
                
    updateDB(key, data)


if __name__ == "__main__":
    main()
    