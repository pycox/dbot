from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 270
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    try:
      driver.find_element(By.CSS_SELECTOR, "button#onetrust-accept-btn-handler").click()
    except:
      print("No Cookie Button")

    time.sleep(4)
    try:
      driver.find_element(By.CSS_SELECTOR, "a[href='/Jobs']").click()
    except:
      print("No Jobs button")

    data = []
    flag = True

    while flag:
        time.sleep(4)
        items = driver.find_elements(By.CSS_SELECTOR, "div.attrax-vacancy-tile")
        for item in items:
            link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()
            location = item.find_element(By.CSS_SELECTOR, 'div.attrax-vacancy-tile__option-location-valueset.attrax-vacancy-tile__item-valueset > p.attrax-vacancy-tile__item-value').text.strip()

            data.append(
                [
                    item.find_element(By.CSS_SELECTOR, "a").text.strip(),
                    com,
                    location,
                    link,
                ]
            )
        
        try:
          button = driver.find_element(By.CSS_SELECTOR, 'li.attrax-pagination__next > a')
          if button:
            driver.execute_script("arguments[0].click();", button)
        except:
          flag = False
          print("No more Jobs")

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
