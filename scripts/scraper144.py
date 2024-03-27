from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 144
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    try:
        time.sleep(4)
        driver.find_element(By.CSS_SELECTOR, "button[data-automation-id='distanceLocation']").click()
        time.sleep(2)
        driver.find_element(By.XPATH, "//label[contains(text(), 'London')]").click()
        time.sleep(4)
        driver.find_element(By.XPATH, "//label[contains(text(), 'Fort Lauderdale')]").click()
        time.sleep(4)
        driver.find_element(By.XPATH, "//label[contains(text(), 'New York')]").click()
        time.sleep(4)
        driver.find_element(By.CSS_SELECTOR, "button[data-automation-id='viewAllJobsButton']").click()
        time.sleep(4)
        
        flag = True
        data = []
        
        while flag:
            try:
                time.sleep(4)
                
                items = driver.find_elements(By.CSS_SELECTOR, "li.css-1q2dra3")
                
                for item in items:
                    link = item.find_element(By.CSS_SELECTOR, "a").get_attribute('href')
                                    
                    data.append([
                        item.find_element(By.CSS_SELECTOR, "a").text.strip(),
                        com,
                        item.find_element(By.CSS_SELECTOR, "dd").text.strip(),
                        link
                    ])
                        
                if len(driver.find_elements(By.CSS_SELECTOR, "button[data-uxi-element-id='next']")) > 0: 
                    driver.find_element(By.CSS_SELECTOR, "button[data-uxi-element-id='next']").click()
                else: 
                    flag = False
                    break
                
            except Exception as e:
                flag = False

        updateDB(key, data)
    except Exception as e:
        print(f"Scraper{key} cookiee button: {e}")



if __name__ == "__main__":
    main()
    