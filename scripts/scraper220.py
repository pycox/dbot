from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 220
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    flag = True
    while flag:
      try:
        button = driver.find_element(By.CSS_SELECTOR, "div.flex.justify-center > button").click()
        time.sleep(4)
      except:
        flag = False
        print("No more load button")

    items = driver.find_elements(By.CSS_SELECTOR, "div.comp-listing-vacancy_vacancy_item__RGJz4.vacancy-item")

    data = []
    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()
        location = item.find_element(By.CSS_SELECTOR, 'div.comp-listing-vacancy_meta_data__Ks_yc.ss-sp-30 > span').text.strip()

        data.append(
            [
                item.find_element(By.CSS_SELECTOR, "div.fs-title-4.text-greenDark.ss-sp-40").text.strip(),
                com,
                location,
                link,
            ]
        )

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
