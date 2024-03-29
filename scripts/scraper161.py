from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time
import math


def main():
    key = 161
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # time.sleep(4)

    # try:
    #     driver.find_element(
    #         By.CSS_SELECTOR,
    #         "button#cookie-accept",
    #     ).click()
    # except Exception as e:
    #     print(f"Scraper{key} cookiee button: {e}")

    time.sleep(2)

    total = int(
        driver.find_element(
            By.CSS_SELECTOR, ".paginationLabel b:last-child"
        ).text.strip()
    )

    data = []

    for i in range(0, math.floor(total / 25)):
        if i != 0:
            driver.get(
                f"https://jobs.knightfrank.com/search/?q=&sortColumn=referencedate&sortDirection=desc&searchby=location&d=15&startrow={i * 25}"
            )

        time.sleep(4)

        items = driver.find_elements(By.CSS_SELECTOR, "tr.data-row")

        for item in items:
            link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()
            location = item.find_element(By.CSS_SELECTOR, "td.colLocation").text.strip()

            if location.split(",")[1].strip() in ["GB", "US"]:
                data.append(
                    [
                        item.find_element(By.CSS_SELECTOR, "td.colTitle").text.strip(),
                        com,
                        location,
                        link,
                    ]
                )

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
