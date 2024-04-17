from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 286
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    try:
      button = driver.find_element(By.CSS_SELECTOR, "a.RichTextBlocklink")
      if button:
        driver.execute_script("arguments[0].click();", button)
    except:
      print("No Listing Page")

    time.sleep(4)

    # items = driver.find_elements(By.CSS_SELECTOR, "table.MuiTable-root-630 > tbody > tr")

    data = []

    # for item in items:
    #     link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()
    #     location = item.find_element(By.CSS_SELECTOR, 'div.MuiBox-root-292 > p.MuiTypography-root-413').text.strip()

    #     for str in ['London', 'New York', 'San Francisco', 'United States', 'United Kingdom', 'UK', 'USA', 'US']:
    #         if (str in location):
    #             data.append(
    #                 [
    #                     item.find_element(By.CSS_SELECTOR, "a").text.strip(),
    #                     com,
    #                     location,
    #                     link,
    #                 ]
    #             )
    #             break

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
