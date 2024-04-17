from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 259
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    data = []
    flag = True

    while flag:
        time.sleep(4)
        items = driver.find_elements(By.CSS_SELECTOR, "section.apply-details__container")
        
        for item in items:
            link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()
            location = item.find_element(By.CSS_SELECTOR, 'p > span').text.strip()

            data.append(
                [
                    item.find_element(By.CSS_SELECTOR, "a").text.strip(),
                    com,
                    location,
                    link,
                ]
            )
        
        try:
          driver.find_element(By.CSS_SELECTOR, 'a.button.next').click()
        except:
          flag = False
          print("No more Jobs")

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
