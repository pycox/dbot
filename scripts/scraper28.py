from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from bs4 import BeautifulSoup
from utils import readUrl, updateDB
import time


def main():
    key = 28
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(8)
    
    try:
        driver.find_element(By.CSS_SELECTOR, 'button#hs-eu-confirmation-button').click()
    except Exception as e:
        print(f'Scraper{key} cookiee button: {e}')
        
    time.sleep(10)
    
    items = driver.find_elements(By.CSS_SELECTOR, 'div.job')
    
    data = []
    
    for item in items:
        link = item.find_element(By.CSS_SELECTOR, 'a').get_attribute("href").strip()
        soup = BeautifulSoup(item.get_attribute('outerHTML'), 'html.parser')
        location = soup.find('p').text.strip()
        title = soup.find('h2').text.strip()
        
        data.append([title, com, location, link])
        
        print(location, title)
        
    updateDB(key, data)


if __name__ == "__main__":
    main()
    