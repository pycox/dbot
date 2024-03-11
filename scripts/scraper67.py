from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 67
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(8)

    data = []

    items = driver.find_elements(By.CSS_SELECTOR, 'li[data-ui="job"]')

    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
        location = item.find_element(By.CSS_SELECTOR, 'span[data-ui="job-location"]').text.strip()

        if location.split(',')[-1].strip() in ["United Kingdom", "United State"]:
            data.append(
                [
                    item.find_element(
                        By.CSS_SELECTOR, 'h3[data-ui="job-title"]'
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
