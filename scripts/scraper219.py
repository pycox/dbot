from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 219
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    data = []
    flag = True
    while flag:
      time.sleep(4)
      items = driver.find_elements(By.CSS_SELECTOR, "li.jobs-list-item")
      for item in items:
          try:
            link = item.find_element(By.CSS_SELECTOR, "a[data-ph-at-id='job-link']").get_attribute("href").strip()
            location = item.find_element(By.CSS_SELECTOR, 'span[data-ph-id="ph-page-element-page11-z1v2dX"]').text.strip()

            for str in ['London', 'New York', 'San Francisco', 'United States', 'United Kingdom', 'UK', 'USA', 'US', 'GB']:
                if (str in location):
                    data.append(
                        [
                            item.find_element(By.CSS_SELECTOR, "span[data-ph-id='ph-page-element-page11-Bsl6iT']").text.strip(),
                            com,
                            location,
                            link,
                        ]
                    )
                    break
          except:
            print("No Job")

      try:
        button = driver.find_element(By.CSS_SELECTOR, "a.next-btn.au-target").click()
        time.sleep(4)
      except:
        flag = False
        print("No more pages")

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
