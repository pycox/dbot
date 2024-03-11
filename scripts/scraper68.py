from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 68
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(8)

    try:
        driver.find_element(
            By.XPATH, "//button[contains(text(), 'Accept all cookies')]"
        ).click()
    except Exception as e:
        print(f"Scraper{key} cookie Button: {e}")

    time.sleep(4)

    data = []

    items = driver.find_elements(By.CSS_SELECTOR, "li.z-career-job-card-image")

    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
        location = (
            item.find_element(By.CSS_SELECTOR, "div.text-md").text.strip().split("·")
        )[1]

        for str in [
            "London",
            "New York",
            "San Francisco",
            "United States",
            "United Kingdom",
        ]:
            if str in location:
                data.append(
                    [
                        item.find_element(
                            By.CSS_SELECTOR, "span.text-block-base-link"
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
