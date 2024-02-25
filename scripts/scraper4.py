from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 4
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
        
    time.sleep(2)
    
    flag = True
    data = []
    
    while flag:
        try:
            time.sleep(4)
            
            items = driver.find_elements(By.CSS_SELECTOR, "div.career-hold")
            
            for item in items:
                                
                data.append([
                    item.find_element(By.CSS_SELECTOR, "h5").text.strip(),
                    com,
                    item.find_element(By.XPATH, "//div[strong = 'Location:']").text.split(':', 1)[1].strip(),
                    item.find_element(By.CSS_SELECTOR, "a").get_attribute('href')
                ])
                
            nextBtn = driver.find_element(By.CSS_SELECTOR, 'ul.pagination').find_elements(By.CSS_SELECTOR, 'li')[-2]

            if not 'disabled' in nextBtn.get_attribute('class'):
                nextBtn.click()
            else:
                flag = False
        except:
            flag = False
            
    updateDB(key, data)
    
    
if __name__ == "__main__":
    main()
    
    
    