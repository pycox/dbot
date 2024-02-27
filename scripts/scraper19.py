from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 19
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(4)
    
    iframe = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(iframe)
    
    try:
        driver.find_element(By.CSS_SELECTOR, 'button').click()
    except Exception as e:
        print(f'Scraper{key} cookiee button: {e}')
        
    time.sleep(20)
    
    driver.switch_to.default_content()
    
    data = []
   
    items = driver.find_elements(By.CSS_SELECTOR, "tbody > tr")[1:-2]
            
    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute('href')
        location = item.find_element(By.CSS_SELECTOR, "td:nth-of-type(6) > span:last-child").text.strip()
        
        data.append([
            item.find_element(By.CSS_SELECTOR, "a").text.strip(),
            com,
            location,
            link
        ])
        
    updateDB(key, data)


if __name__ == "__main__":
    main()
    