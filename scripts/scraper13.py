from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 13
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(10)
    
    try:
        driver.find_element(By.CSS_SELECTOR, "button#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll").click()
    except Exception as e:
        print(f'Scraper{key} cookiee button: {e}')
    
    flag = True
    data = []
    
    while flag:
        try:
            time.sleep(8)
            
            items = driver.find_elements(By.CSS_SELECTOR, "div.job-listing__job")
            
            for item in items:
                link = item.find_element(By.CSS_SELECTOR, "a").get_attribute('href')
                location = item.find_element(By.CSS_SELECTOR, 'p.city').text.strip()
                        
                if location in ["London"]:        
                    data.append([
                        item.find_element(By.CSS_SELECTOR, "h3").text.strip(),
                        com,
                        location,
                        link
                    ])
            
            nextBtn = driver.find_elements(By.CSS_SELECTOR, 'li.paginationjs-next')

            if len(nextBtn) > 0:
                nextBtn[0].click()
            else:
                flag = False
        except:
            flag = False
            
    updateDB(key, data)
    
    
if __name__ == "__main__":
    main()
    
    
    
    