from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 153
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    items = driver.find_elements(By.CSS_SELECTOR, "a.vacancies_item")

    data = []

    for item in items:
        link = item.get_attribute("href").strip()

        data.append(
            [
                item.find_element(By.CSS_SELECTOR, "h5").text.strip(),
                com,
                item.find_element(By.CSS_SELECTOR, "p").text.strip(),
                link,
            ]
        )

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
