from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 196
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    try:
        driver.find_element(
            By.CSS_SELECTOR,
            "button#CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll",
        ).click()
    except Exception as e:
        print(f"Scraper{key} cookie Button: {e}")

    time.sleep(4)

    items = driver.find_elements(By.CSS_SELECTOR, "div.CareersSearch_role__P6kRm")

    data = []

    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "div.CareersSearch_role__cta__UE_MB > a").get_attribute("href").strip()
        location = item.find_element(By.CSS_SELECTOR, 'p:last-child').text.strip()

        for str in ['London', 'New York', 'San Francisco', 'United States', 'United Kingdom', 'UK', 'USA', 'US']:
            if (str in location):
                data.append(
                    [
                        item.find_element(By.CSS_SELECTOR, "div > h4").text.strip(),
                        com,
                        location,
                        link,
                    ]
                )
                break

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
