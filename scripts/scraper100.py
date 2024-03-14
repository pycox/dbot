from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 100
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)
    time.sleep(4)

    try:
        driver.find_element(By.CSS_SELECTOR, "button#ensCloseBanner").click()
    except Exception as e:
        print(f"Scraper{key} cookie Button: {e}")

    time.sleep(4)

    driver.execute_script("window.scrollTo(0, 800)")

    time.sleep(4)

    items = driver.find_elements(By.CSS_SELECTOR, "div._1xgeez75")

    data = []

    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()

        data.append(
            [
                item.find_element(By.CSS_SELECTOR, "h3").text.strip(),
                com,
                item.find_element(By.CSS_SELECTOR, "p._1xgeez73").text.strip(),
                link,
            ]
        )
        
    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
