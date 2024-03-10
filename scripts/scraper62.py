from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 62
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(8)

    try:
        driver.find_element(
            By.CSS_SELECTOR,
            "button#accept-recommended-btn-handler",
        ).click()
    except Exception as e:
        print(f"Scraper{key} cookiee button: {e}")
        
    time.sleep(4)

    items = driver.find_elements(By.CSS_SELECTOR, "a.job-offer")

    data = []

    for item in items:
        link = item.get_attribute("href").strip()
        location = item.find_element(
            By.CSS_SELECTOR, "p.job-offer__location"
        ).text.strip()

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
                        item.find_element(By.CSS_SELECTOR, "p").text.strip(),
                        com,
                        location,
                        link,
                    ]
                )

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
