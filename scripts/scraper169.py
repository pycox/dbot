from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 169
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)
    
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    
    time.sleep(2)

    data = []

    items = driver.find_elements(By.CSS_SELECTOR, "div.jobs-card")

    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
        location = item.find_element(
            By.CSS_SELECTOR, "div.card--where-about"
        ).text.split('·')[0].strip().replace('\n', '')
        
        if location.split(',')[-1].strip() in['United Kingdom', 'United States']:
            data.append(
                [
                    item.find_element(By.CSS_SELECTOR, "h2.card--title").text.strip(),
                    com,
                    location,
                    link,
                ]
            )

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
