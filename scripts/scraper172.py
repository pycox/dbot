from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 172
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    try:
        driver.find_element(
            By.CSS_SELECTOR,
            "button#onetrust-accept-btn-handler",
        ).click()
    except Exception as e:
        print(f"Scraper{key} cookie Button: {e}")

    flag = True
    data = []

    while flag:
        try:
            time.sleep(4)

            items = driver.find_elements(By.CSS_SELECTOR, "li.job-card")

            for item in items:
                link = item.find_element(By.CSS_SELECTOR, "h1").get_attribute("href")
                location = item.find_element(By.CSS_SELECTOR, "li").text.strip()

                data.append(
                    [
                        item.find_element(By.CSS_SELECTOR, "h1").text.strip(),
                        com,
                        location,
                        link,
                    ]
                )

            nextBtn = driver.find_elements(
                By.XPATH, "//a[contains(text(), 'Next Page')]"
            )

            if (
                len(
                    nextBtn,
                )
                > 0
            ):
                nextBtn[0].click()
            else:
                flag = False
                break

        except Exception as e:
            print(e)
            flag = False

    driver.quit()
    
    updateDB(key, data)


if __name__ == "__main__":
    main()
