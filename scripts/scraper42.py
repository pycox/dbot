from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 42
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    try:
        driver.find_element(
            By.CSS_SELECTOR, "a#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll"
        ).click()
    except Exception as e:
        print(f"Scraper{key} cookiee button: {e}")

    time.sleep(4)
    
    data = []

    locations = driver.find_elements(By.CSS_SELECTOR, "h2.whr-group")
    doms = driver.find_elements(By.CSS_SELECTOR, "ul.whr-items")

    for i in range(0, len(locations)):
        location = locations[i].text.strip()
        items = doms[i].find_elements(By.CSS_SELECTOR, "li.whr-item")
        
        for item in items:
            link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()
            title = item.find_element(By.CSS_SELECTOR, "h3.whr-title").text.strip()
            
            data.append(
                [
                    title,
                    com,
                    location,
                    link,
                ]
            )

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
