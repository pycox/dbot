from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 125
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    items = driver.find_elements(By.CSS_SELECTOR, "div#archive > div > div")

    data = []

    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()
        title = item.find_element(By.CSS_SELECTOR, "h4").text.strip()
        location = title.split("–")[-1].strip()
        print(title)

        if location in ["Kendal", "USA"]:

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
