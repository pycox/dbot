from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 45
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

            items = driver.find_elements(By.CSS_SELECTOR, "div.rowContainerHolder")

            for item in items:
                link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                location = item.find_element(
                    By.CSS_SELECTOR, "span.vacancyColumn"
                ).text.strip()

                for str in [
                    "London",
                    "New York",
                    "San Francisco",
                    "United States",
                    "United Kingdom",
                ]:
                    if str in location:

                        data.append(
                            [
                                item.find_element(
                                    By.CSS_SELECTOR, "div.rowHeader"
                                ).text.strip(),
                                com,
                                location,
                                link,
                            ]
                        )

                        break

            nextBtn = driver.find_element(By.CSS_SELECTOR, "a.scroller_movenext")

            if nextBtn.get_attribute("disabled") == "true":

                flag = False
                break
            else:
                nextBtn.click()
        except:
            flag = False

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
