from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 76
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    data = []

    items = driver.find_elements(By.CSS_SELECTOR, "div > h2 + ul")

    for item in items:
        title = item.find_element(
            By.XPATH, "./preceding-sibling::h2[1]/p/span"
        ).text.strip()
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
        location = item.find_element(
            By.XPATH, "//li[contains(text(), 'Location')]"
        ).text.strip()

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
