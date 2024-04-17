from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 283
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    data = []
    flag = True

    while flag:
        time.sleep(4)
        items = driver.find_elements(By.CSS_SELECTOR, "li.jobs-list-item")
        for item in items:
            link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()
            location = item.find_element(By.CSS_SELECTOR, 'span.job-location').text.strip()

            for str in ['London', 'New York', 'San Francisco', 'United States', 'United Kingdom', 'UK', 'USA', 'US']:
                if (str in location):
                    data.append(
                        [
                            item.find_element(By.CSS_SELECTOR, "span[data-ph-id='ph-page-element-page23-0m1Gq1']").text.strip(),
                            com,
                            location,
                            link,
                        ]
                    )
                    break

        try:
          driver.find_element(By.CSS_SELECTOR, "a[data-ph-at-id='pagination-next-link']").click()
        except:
          flag = False
          print("No More Jobs")

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
