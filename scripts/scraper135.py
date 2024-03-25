from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 135
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(8)

    items = len(driver.find_elements(By.CSS_SELECTOR, "div.current-openings-item"))

    data = []

    for i in range(0, items):
        item = driver.find_elements(By.CSS_SELECTOR, "div.current-openings-item")[i]
        
        title = item.find_element(
            By.CSS_SELECTOR, "span.current-opening-title"
        ).text.strip()
        location = item.find_element(
            By.CSS_SELECTOR, "div.current-opening-locations"
        ).text.strip()

        item.find_element(By.CSS_SELECTOR, "button").click()

        time.sleep(4)

        data.append([title, com, location, driver.current_url])

        driver.find_element(
            By.CSS_SELECTOR, "button#recruitment_jobDescription_back"
        ).click()

        time.sleep(4)
        
    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
