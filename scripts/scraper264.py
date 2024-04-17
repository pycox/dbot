from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 264
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    flag = True
    while flag:
      try:
        time.sleep(4)
        driver.find_element(By.CSS_SELECTOR, "div.mt-10.flex.justify-center > button").click()
      except:
        flag = False
        print("No more Load Button")

    time.sleep(4)
    items = driver.find_elements(By.CSS_SELECTOR, "div.grid.grid-cols-1.gap-6 > a")

    data = []
    for item in items:
        link = item.get_attribute("href").strip()
        location = item.find_element(By.CSS_SELECTOR, 'span.body-small.body-bold.text-grey-secondary').text.strip()

        for str in ['London', 'New York', 'San Francisco', 'United States', 'United Kingdom', 'UK', 'USA', 'US']:
            if (str in location):
                data.append(
                    [
                        item.find_element(By.CSS_SELECTOR, "h4").text.strip(),
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
