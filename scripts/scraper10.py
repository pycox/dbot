from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 10
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(10)
    
    items = driver.find_elements(By.CSS_SELECTOR, 'li.css-1q2dra3')
    
    data = []
    
    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()
        locationDom = item.find_element(By.CSS_SELECTOR, 'div[data-automation-id="locations"]')
            
        data.append([
            item.find_element(By.CSS_SELECTOR, "h3").text.strip(),
            com,
            locationDom.find_element(By.CSS_SELECTOR, 'dd').text.strip(),
            link
        ])
                
    updateDB(key, data)


if __name__ == "__main__":
    main()
    