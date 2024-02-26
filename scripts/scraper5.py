from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 5
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(4)
    
    flag = True
    data = []
    
    while flag:
        try:
            time.sleep(4)
            
            nextBtn = driver.find_elements(By.CSS_SELECTOR, 'div#load-more-jobs')

            if len(nextBtn) > 0:
                nextBtn[0].find_element(By.CSS_SELECTOR, 'a').click()
            else:
                flag = False
        except:
            flag = False
    
    items = driver.find_elements(By.CSS_SELECTOR, "div.job")
    
    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute('href')
                        
        data.append([
            item.find_element(By.CSS_SELECTOR, "a").text.strip(),
            com,
            item.find_element(By.CSS_SELECTOR, 'div.sub-text').text.strip(),
            link
        ])
            
    updateDB(key, data)
    
    
if __name__ == "__main__":
    main()
    
    
    