from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 49
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    try:
        driver.find_element(By.CSS_SELECTOR, "button.cky-btn-accept").click()
    except Exception as e:
        print(f"Scraper{key} cookiee button: {e}")

    data = []
    flag = True

    while flag:
        try:
            time.sleep(4)

            driver.find_element(By.CSS_SELECTOR, "a.load_more_jobs").click()

        except Exception as e:
            flag = False
            break

    items = driver.find_elements(By.CSS_SELECTOR, "li.job_listing")

    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()
        title = item.find_element(By.CSS_SELECTOR, "div.position").text.strip()
        location = item.find_element(By.CSS_SELECTOR, "div.location").text.strip()

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
