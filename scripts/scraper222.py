from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 222
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    addresses = driver.find_elements(By.CSS_SELECTOR, "div.comeet-g-r")

    data = []

    for address in addresses:
        location = address.find_element(By.CSS_SELECTOR, 'div.comeet-list.comeet-group-name > a').text.strip()
        
        for str in ['London', 'New York', 'San Francisco', 'United States', 'United Kingdom', 'UK', 'USA', 'US']:
            if (str in location):
              
              items = address.find_elements(By.CSS_SELECTOR, 'ul.comeet-positions-list > li')
              for item in items:
                  link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()
                  data.append(
                      [
                          item.find_element(By.CSS_SELECTOR, "div.comeet-position-name").text.strip(),
                          com,
                          location,
                          link,
                      ]
                  )

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
