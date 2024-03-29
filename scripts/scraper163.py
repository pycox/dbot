from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 163
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    # time.sleep(4)

    # try:
    #     driver.find_element(By.CSS_SELECTOR, "a#hs-eu-confirmation-button").click()
    # except Exception as e:
    #     print(f"Scraper{key} cookiee button: {e}")

    time.sleep(4)

    data = []

    # items = driver.find_elements(
    #     By.CSS_SELECTOR, "div[data-content-type='text'][data-element='main']"
    # )

    # for item in items:
    #     title = (
    #         item.find_element(
    #             By.CSS_SELECTOR,
    #             "strong",
    #         ).text
    #         if item.find_element(
    #             By.CSS_SELECTOR,
    #             "strong",
    #         )
    #         else None
    #     )

    #     if title is None:
    #         continue

    #     # link = (
    #     #     item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()
    #     #     if item.find_element(
    #     #         By.CSS_SELECTOR,
    #     #         "a",
    #     #     )
    #     #     else None
    #     # )

    #     # if link is None:
    #     #     continue

    #     # location = item.find_element(
    #     #     By.XPATH,
    #     #     ".//strong[contains(text(), 'Location:')]/following-sibling::*[1]",
    #     # ).text

    #     data.append(
    #         [
    #             title,
    #             com,
    #             # location.text.strip(),
    #             # link,
    #         ]
    #     )

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
