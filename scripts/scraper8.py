from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 8
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(4)
    
    try:
        driver.find_element(By.CSS_SELECTOR, "button#cc-saveAll-startBtn").click()
    except Exception as e:
        print(f'Scraper{key} cookiee button: {e}')
        
    flag = True
    data = []
    
    while flag:
        try:
            time.sleep(4)
            
            nextBtn = driver.find_elements(By.CSS_SELECTOR, 'a.m-auto')

            if len(nextBtn) > 0:
                nextBtn[0].click()
            else:
                flag = False
        except:
            flag = False
    
    items = driver.find_elements(By.CSS_SELECTOR, "div.job-list-item")
    
    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute('href')
        location = item.find_element(By.CSS_SELECTOR, 'td[data-label="Location"]').text.strip()
                        
        data.append([
            item.find_element(By.CSS_SELECTOR, "h4").text.strip(),
            com,
            location,
            link
        ])
            
    updateDB(key, data)
    
    
if __name__ == "__main__":
    main()
    
    
    