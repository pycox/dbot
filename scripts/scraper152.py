from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 152
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    dom = driver.find_element(By.CSS_SELECTOR, "div._departments_1qwfy_345")

    items = dom.find_elements(By.CSS_SELECTOR, "a")

    data = []

    for item in items:
        link = item.get_attribute("href").strip()

        data.append(
            [
                item.find_element(By.CSS_SELECTOR, "h3").text.strip(),
                com,
                item.find_element(By.CSS_SELECTOR, "p").text.split("•")[1].strip(),
                link,
            ]
        )

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
