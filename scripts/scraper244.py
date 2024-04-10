from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 244
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    flag = True
    while flag:
      try:
        driver.find_element(By.CSS_SELECTOR, 'a#show_more_button').click()
        time.sleep(4)
      except:
        flag = False
        print("No more Jobs")

    items = driver.find_elements(By.CSS_SELECTOR, "ul#jobs_list_container > li")

    data = []

    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()
        try:
          location = item.find_element(By.CSS_SELECTOR, 'div > span:nth-child(3)').text.strip()
        except:
          location = item.find_element(By.CSS_SELECTOR, 'div > span').text.strip()

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
