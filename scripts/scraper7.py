from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 7
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    
    flag = True
    data = []
    newHist = []
    i = 1
    
    time.sleep(4)
    
    while flag:
        try:
            driver.get(f"{url}jobs/search/-1/{i}")
            
            time.sleep(4)
            
            if len(driver.find_element(By.CSS_SELECTOR, "div#results").find_elements(By.CSS_SELECTOR, "div.alert-foo")) > 0: 
                flag = False
                break
            
            items = driver.find_element(By.CSS_SELECTOR, "ul.jobs").find_elements(By.CSS_SELECTOR, 'li')
            
            for item in items:
                link = item.find_element(By.CSS_SELECTOR, "a").get_attribute('href')
                location = item.find_element(By.CSS_SELECTOR, "span[itemprop='address']").text.strip().split(',')[-1].strip()
                
                if location in ['United States', 'United Kingdom']:
                    data.append([
                        item.find_element(By.CSS_SELECTOR, "h3").text.strip(),
                        com,
                        location,
                        link
                    ])
                
                newHist.append(link)
            
            i = i + 1
        except:
            flag = False
            
    updateDB(key, data)
    
    
if __name__ == "__main__":
    main()
    
    
    