from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 24
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    
    time.sleep(4)
    
    try:
        driver.find_element(By.CSS_SELECTOR, 'button#onetrust-accept-btn-handler').click()
    except Exception as e:
        print(f'Scraper{key} cookiee button: {e}')
        
    flag = True
    data = []
    
    while flag:
        try:
            time.sleep(4)
            
            items = driver.find_elements(By.CSS_SELECTOR, "tbody > tr.nx-table-row")
            
            for item in items:
                cols = item.find_elements(By.CSS_SELECTOR, "td")
                link = item.find_element(By.CSS_SELECTOR, 'a').get_attribute('href')
                title = cols[0].text.strip()
                location = cols[3].text.strip()
                
                data.append([
                    title,
                    com,
                    location,
                    f'https://careers.allianz.com{link}'
                ])
            
            nextBtn = driver.find_element(By.CSS_SELECTOR, 'button.nx-pagination__link--next')

            if nextBtn.is_enabled():
                nextBtn.click()
            else:
                flag = False
        except:
            flag = False
            
    updateDB(key, data)


if __name__ == "__main__":
    main()
    