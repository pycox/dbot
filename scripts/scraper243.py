from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 243
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    count = 0
    while count < 3:
      try:
        driver.find_element(By.CSS_SELECTOR, 'a.filters-more').click()
        time.sleep(4)
        count += 1
      except:
        count = 3
        print("No more Jobs")

    items = driver.find_elements(By.CSS_SELECTOR, "a.table-tr.filter-box.tag-active.joblink")

    data = []

    for item in items:
        link = item.get_attribute("href").strip()
        location = item.find_element(By.CSS_SELECTOR, 'div:nth-child(2) > div').text.strip()

        for str in ['London', 'New York', 'San Francisco', 'United States', 'United Kingdom', 'UK', 'USA', 'US']:
            if (str in location):
                data.append(
                    [
                        item.find_element(By.CSS_SELECTOR, "div > div").text.strip(),
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
