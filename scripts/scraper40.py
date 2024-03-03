from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 40
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(10)

    try:
        driver.find_element(
            By.CSS_SELECTOR, "button[data-test='cookie-banner-accept']"
        ).click()
    except Exception as e:
        print(f"Scraper{key} cookie Button: {e}")

    time.sleep(4)

    doms = driver.find_elements(By.XPATH, "//h3[contains(text(), 'US')]")
    doms = doms + driver.find_elements(By.XPATH, "//h3[contains(text(), 'UK')]")

    data = []

    for dom in doms:
        pa = dom.find_element(By.XPATH, "../..")

        location = dom.text.strip()

        items = pa.find_elements(By.CSS_SELECTOR, "a")

        for item in items:
            link = item.get_attribute("href").strip()
            title = item.find_element(By.CSS_SELECTOR, "div > div").text.strip()

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
