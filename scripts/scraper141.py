from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 141
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    try:
        # driver.find_element(By.CSS_SELECTOR, "input.js-consent-all-submit").click()
        driver.find_element(By.CSS_SELECTOR, "button#onetrust-accept-btn-handler").click()
    except Exception as e:
        print(f"Scraper{key} cookie Button: {e}")

    data = []
    items = len(driver.find_elements(By.CSS_SELECTOR, "div.jobs-listing > a.cmp-jobs__list--links"))


    for i in range(0, items):
        item = driver.find_elements(By.CSS_SELECTOR, "div.jobs-listing > a.cmp-jobs__list--links")[i]
        
        title = item.find_element(
            By.CSS_SELECTOR, "span.cmp-jobs__list--content.title"
        ).text.strip()

        country = item.find_element(
            By.CSS_SELECTOR, "span.cmp-jobs__list--content:first-child"
        ).text.strip()

        location = item.find_element(
            By.CSS_SELECTOR, "span.location"
        ).text.strip()

        link = item.get_attribute('href').strip()

        if country.strip() in ["UK", "US"] and country:
            data.append([title, com, country + ' ' + location, link])

        time.sleep(1)
            
    driver.quit()

    updateDB(key, data)

if __name__ == "__main__":
    main()
