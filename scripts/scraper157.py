from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 157
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    try:
        driver.find_element(
            By.CSS_SELECTOR,
            "button#onetrust-accept-btn-handler",
        ).click()
    except Exception as e:
        print(f"Scraper{key} cookie Button: {e}")

    time.sleep(4)

    items = driver.find_elements(By.CSS_SELECTOR, "tbody > tr")

    data = []

    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()

        data.append(
            [
                item.find_element(By.CSS_SELECTOR, "a").text.strip(),
                com,
                item.find_elements(By.CSS_SELECTOR, "td")[2].text.strip(),
                link,
            ]
        )
        
    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
