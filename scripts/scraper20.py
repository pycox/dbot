from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 20
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(4)
    
    try:
        driver.find_element(By.CSS_SELECTOR, 'button#hs-eu-confirmation-button').click()
    except Exception as e:
        print(f'Scraper{key} cookiee button: {e}')
        
    time.sleep(4)
    
    iframe = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(iframe)
    
    items = driver.find_elements(By.CSS_SELECTOR, 'div.opening')
    
    data = []
    
    for item in items:
        link = item.find_element(By.CSS_SELECTOR, 'a').get_attribute("href").strip()
        location = item.find_element(By.CSS_SELECTOR, "span").text.strip()
        
        print(link, location)
            
        for str in ['London', 'New York', 'San Francisco', 'United States', 'United Kingdom']:
            if (str in location):
                data.append([
                    item.find_element(By.CSS_SELECTOR, 'a').text.strip(),
                    com,
                    location,
                    link
                ])
                
                break
                
    updateDB(key, data)


if __name__ == "__main__":
    main()
    