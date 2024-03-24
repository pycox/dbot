from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 133
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    # try:
    #     driver.find_element(
    #         By.CSS_SELECTOR,
    #         "button[data-action='click->common--cookies--alert#acceptAll']",
    #     ).click()
    # except Exception as e:
    #     print(f"Scraper{key} cookie Button: {e}")

    # time.sleep(4)

    dom = driver.find_element(By.CSS_SELECTOR, "ul#jobs_list_container")

    flag = True
    data = []

    while flag:
        try:
            time.sleep(4)

            nextBtn = driver.find_elements(By.CSS_SELECTOR, "a#show_more_button")

            if len(nextBtn) > 0:
                nextBtn[0].click()
            else:
                flag = False
                break
        except:
            flag = False
            break

    items = dom.find_elements(By.CSS_SELECTOR, "li")

    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()

        data.append(
            [
                item.find_element(By.CSS_SELECTOR, "span").text.strip(),
                com,
                "UK",
                link,
            ]
        )

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
