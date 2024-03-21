from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 130
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    data = []
    flag = True

    while flag:
        try:
            time.sleep(4)

            driver.find_element(
                By.CSS_SELECTOR, 'button[data-ui="load-more-button"]'
            ).click()

        except Exception as e:
            flag = False
            break

    items = driver.find_elements(By.CSS_SELECTOR, 'li[data-ui="job"]')

    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()
        title = item.find_element(By.CSS_SELECTOR, "h3").text.strip()
        location = item.find_element(
            By.CSS_SELECTOR, 'span[data-ui="job-location"]'
        ).text.strip()

        if location.split(",")[-1].strip() in ["United Kingdom", "United States"]:
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
