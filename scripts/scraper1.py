from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readHistory, updateHistory, readUrl, updateDB
import time


def main():
    key = 1
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(4)
    
    # try:
    #     driver.find_element(By.CSS_SELECTOR, "a.js--click-setCookie").click()
    # except Exception as e:
    #     print(f'Scraper{key} cookiee button: {e}')
        
    # time.sleep(4)
    
    items = driver.find_elements(By.CSS_SELECTOR, "div.sc-uzptka-1")
    
    newHist = []
    
    data = []
    
    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()
        location = item.find_element(By.CSS_SELECTOR, "span").text.strip()
        
        if not link in readHistory(key) and location.split(',')[-1].strip() in ['United States', 'United Kingdom']:
            data.append([
                item.find_element(By.CSS_SELECTOR, "a").text.strip(),
                com,
                location,
                link
            ])
        
        newHist.append(link)
        
    updateDB(data)
    
    updateHistory(f'{key}', newHist)


if __name__ == "__main__":
    main()