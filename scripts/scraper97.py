from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 97
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(8)

    iframe = driver.find_element(By.TAG_NAME, "iframe")
    driver.switch_to.frame(iframe)

    driver.find_element(By.CSS_SELECTOR, "input[name='tbe_cws_submit']").click()

    time.sleep(8)

    dom = driver.find_element(By.CSS_SELECTOR, "table#cws-search-results")
    items = dom.find_elements(By.CSS_SELECTOR, "tr")[1:]

    data = []

    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()

        data.append(
            [
                item.find_element(By.CSS_SELECTOR, "td").text.strip(),
                com,
                item.find_elements(By.CSS_SELECTOR, "td")[1].text.strip(),
                link,
            ]
        )

    driver.quit()
    
    updateDB(key, data)


if __name__ == "__main__":
    main()
