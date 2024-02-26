from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 16
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    driver.get(url)
    
    time.sleep(4)
    
    try:
        driver.find_element(By.CSS_SELECTOR, "div[color='buttonPrimaryText']").click()
    except Exception as e:
        print(f'Scraper{key} cookie Button: {e}')
        
    time.sleep(2)
    
    items = driver.find_elements(By.CSS_SELECTOR, "div.hNOmHV")
    
    data = []
    
    for item in items:
        item.click()
        
        time.sleep(1)
        
        dom = driver.find_element(By.CSS_SELECTOR, 'div[data-testid="hit-result-preview"]')
        
        location = dom.find_element(By.CSS_SELECTOR, 'div.khvRUu').text.strip()
        
        if location.split(',')[-1].strip() in ['United Kingdom', 'United States']:
            data.append([
                dom.find_element(By.CSS_SELECTOR, 'div.eCRcon').text.strip(),
                com,
                location,
                driver.current_url
            ])
        
    updateDB(key, data)


if __name__ == "__main__":
    main()