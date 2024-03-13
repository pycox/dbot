from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 96
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    driver.execute_script("window.scrollTo(0, 1000)")
    driver.find_element(By.CSS_SELECTOR, "div").click()
    time.sleep(4)

    time.sleep(8)

    items = driver.find_elements(By.CSS_SELECTOR, "div.jobs-list > div")

    data = []

    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()

        data.append(
            [
                item.find_element(By.CSS_SELECTOR, "a").text.strip(),
                com,
                item.find_elements(By.CSS_SELECTOR, "span")[1].text.strip(),
                link,
            ]
        )

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
