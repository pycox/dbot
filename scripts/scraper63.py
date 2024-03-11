from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 63
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(8)

    try:
        driver.find_element(
            By.CSS_SELECTOR,
            "div.cookie-consent__actions > button",
        ).click()
    except Exception as e:
        print(f"Scraper{key} cookiee button: {e}")

    time.sleep(4)

    items = driver.find_elements(By.CSS_SELECTOR, 'li[data-qa="searchResultItem"]')

    data = []

    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()
        location = item.find_element(
            By.CSS_SELECTOR, "div.job-tile__subheader > span"
        ).text.strip()

        data.append(
            [
                item.find_element(
                    By.CSS_SELECTOR, "div.job-tile__header > span"
                ).text.strip(),
                com,
                location,
                link,
            ]
        )

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
