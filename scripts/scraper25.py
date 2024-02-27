from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 25
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
        
    time.sleep(4)
    
    items = driver.find_elements(By.CSS_SELECTOR, 'div.elementor-post__card')
    
    data = []
    
    for item in items:
        link = item.find_element(By.CSS_SELECTOR, 'a').get_attribute("href").strip()
        title = item.find_element(By.CSS_SELECTOR, 'a').text.strip()
        
        data.append([title, com, 'UK', link])
        
    updateDB(key, data)


if __name__ == "__main__":
    main()
    