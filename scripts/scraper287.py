from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 287
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    try:
      button = driver.find_element(By.CSS_SELECTOR, "a[aria-label='See all vacancies']")
      if button:
        driver.execute_script("arguments[0].click();", button)
    except:
      print("No Listing Page")

    time.sleep(4)
    driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
    time.sleep(4)

    items = driver.find_elements(By.CSS_SELECTOR, "div.ds-grid__col > div > ul > li")

    data = []

    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()
        location = item.find_element(By.CSS_SELECTOR, 'div.ds-grid__col:nth-child(3) > button').text.strip()

        for str in ['London', 'New York', 'San Francisco', 'United States', 'United Kingdom', 'UK', 'USA', 'US']:
            if (str in location):
                data.append(
                    [
                        item.find_element(By.CSS_SELECTOR, "span").text.strip(),
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
