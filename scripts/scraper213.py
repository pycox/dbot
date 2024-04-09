from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 213
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    try:
        driver.find_element(By.CSS_SELECTOR, "button.iubenda-cs-reject-btn.iubenda-cs-btn-primary").click()
    except Exception as e:
        print(f'Scraper{key} cookiee button: {e}')
        
    time.sleep(4)

    items = driver.find_elements(By.CSS_SELECTOR, "div.x-callout.left-text")

    data = []

    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()

        data.append(
            [
                item.find_element(By.CSS_SELECTOR, "h2.h-callout").text.strip(),
                com,
                "UK",
                link,
            ]
        )

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
