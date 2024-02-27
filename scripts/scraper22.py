from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 22
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(4)
    
    items = driver.find_elements(By.CSS_SELECTOR, 'div.attrax-vacancy-tile')
    
    data = []
    
    for item in items:
        link = item.find_element(By.CSS_SELECTOR, 'a').get_attribute("href").strip()
        location = item.find_element(By.CSS_SELECTOR, 'div.attrax-vacancy-tile__option-location-valueset').text.strip()
        
        if location in ['London', 'New York']:
            data.append([
                item.find_element(By.CSS_SELECTOR, 'a').text.strip(),
                com,
                "United Kindom",
                link
            ])
                
    updateDB(key, data)


if __name__ == "__main__":
    main()
    