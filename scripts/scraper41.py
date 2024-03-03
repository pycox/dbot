from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 41
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(8)

    try:
        driver.find_element(By.CSS_SELECTOR, "div.dialog-message").find_element(
            By.CSS_SELECTOR, "a.elementor-button"
        ).click()
    except Exception as e:
        print(f"Scraper7 cookiee button: {e}")

    time.sleep(10)

    iframe = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(iframe)

    dom = driver.find_element(By.CSS_SELECTOR, "div#main")
    items = dom.find_elements(By.CSS_SELECTOR, "section")

    data = []

    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()

        data.append(
            [
                item.find_element(By.CSS_SELECTOR, "a").text.strip(),
                com,
                item.find_element(By.CSS_SELECTOR, "span.location").text.strip(),
                link,
            ]
        )

    updateDB(key, data)


if __name__ == "__main__":
    main()
