from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 239
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
          link = item.find_element(By.CSS_SELECTOR, "a[data-ph-at-id='job-link']").get_attribute("href").strip()
          location = item.find_element(By.CSS_SELECTOR, 'span[data-ph-at-id="job-multi-location-item"]').text.strip()
          location = location.replace("Location", "").replace("\n", "")
          
          for str in ['London', 'New York', 'San Francisco', 'United States', 'United Kingdom', 'UK', 'USA', 'US', 'GB', "United States Of America"]:
              if (str in location):
                  data.append(
                      [
                          item.find_element(By.CSS_SELECTOR, "span[data-ph-id='ph-page-element-page13-S1igwT']").text.strip(),
                          com,
                          location,
                          link,
                      ]
                  )
                  break
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
