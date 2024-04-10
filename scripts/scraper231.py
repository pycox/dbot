from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 231
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    items = driver.find_elements(By.CSS_SELECTOR, "div.job-vacancy")

    data = []

    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "div.job-vacancy__apply > a").get_attribute("href").strip()
        location = item.find_element(By.CSS_SELECTOR, 'div.job-vacancy__table > div:nth-child(3)').text.strip()
        location = location.replace("Location:", "").strip()

        data.append(
            [
                item.find_element(By.CSS_SELECTOR, "div.job-vacancy__title").text.strip(),
                com,
                location,
                link,
            ]
        )

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
