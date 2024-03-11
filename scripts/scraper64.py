from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 64
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    flag = True
    data = []

    while flag:
        try:
            time.sleep(4)

            items = driver.find_elements(By.CSS_SELECTOR, "div.position_opening")

            for item in items:
                link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                location = item.find_elements(By.CSS_SELECTOR, "div.panel-body > p")[
                    1
                ].text.strip()
                
                print(item.find_element(By.CSS_SELECTOR, "h1").text.strip())

                data.append(
                    [
                        item.find_element(By.CSS_SELECTOR, "h1").text.strip(),
                        com,
                        location,
                        link,
                    ]
                )

            nextBtn = driver.find_elements(By.CSS_SELECTOR, 'a[rel="next"]')

            if len(nextBtn) > 0:
                nextBtn[0].click()
            else:
                flag = False
        except:
            flag = False

    updateDB(key, data)


if __name__ == "__main__":
    main()
