from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 134
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    items = driver.find_element(By.CSS_SELECTOR, "div#all").find_elements(
        By.CSS_SELECTOR, "a.job-box"
    )

    data = []

    for item in items:
        link = item.get_attribute("href").strip()
        title = item.find_element(By.CSS_SELECTOR, "div.jb-title").text.strip()
        location = (
            item.find_element(By.CSS_SELECTOR, "div.jb-description")
            .text.split("·")[-1]
            .strip()
        )

        for str in [
            "London",
            "New York",
            "San Francisco",
            "US",
            "UK",
        ]:
            if str in location:
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
