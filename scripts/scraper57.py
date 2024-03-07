from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 57
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    try:
        driver.find_element(
            By.CSS_SELECTOR,
            "button#gdpr-button",
        ).click()
    except Exception as e:
        print(f"Scraper{key} cookiee button: {e}")

    time.sleep(2)

    items = driver.find_elements(By.CSS_SELECTOR, "ul.search-results-list > li")

    data = []

    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()
        location = item.find_element(By.CSS_SELECTOR, "span.job-location").text.strip()

        if location.split(",")[-1].strip() in ["United Kingdom", "United States"]:
            data.append(
                [
                    item.find_element(By.CSS_SELECTOR, "h2").text.strip(),
                    com,
                    location,
                    link,
                ]
            )

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
