from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 108
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    try:
        driver.find_element(By.CSS_SELECTOR, "div.button-agree").click()
    except Exception as e:
        print(f"Scraper{key} cookiee button: {e}")

    time.sleep(4)

    # items = driver.find_elements(By.CSS_SELECTOR, "ul > div")

    data = []

    # for item in items:
    #     link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()
    #     location = item.find_element(By.CSS_SELECTOR, "p.jss-f72").text.strip()

    #     for str in [
    #         "London",
    #         "New York",
    #         "San Francisco",
    #         "United States",
    #         "United Kingdom",
    #     ]:
    #         if str in location:
    #             data.append(
    #                 [
    #                     item.find_element(By.CSS_SELECTOR, "a").text.strip(),
    #                     com,
    #                     location,
    #                     link,
    #                 ]
    #             )

    #             break

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
