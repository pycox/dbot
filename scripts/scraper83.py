from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 83
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    try:
        driver.find_element(By.CSS_SELECTOR, "button#cookie-acknowledge").click()
    except Exception as e:
        print(f"Scraper{key} cookie button: {e}")

    flag = True

    while flag:
        try:
            time.sleep(2)

            loadBtn = driver.find_element(By.CSS_SELECTOR, "button#tile-more-results")

            loadBtn.click()
        except Exception as e:
            flag = False

    dom = driver.find_element(By.CSS_SELECTOR, "ul#job-tile-list")

    items = dom.find_elements(By.CSS_SELECTOR, "li")

    data = []

    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()
        location = (
            item.find_element(By.XPATH, ".//span[contains(text(), 'Location')]")
            .find_element(By.XPATH, "./following-sibling::div")
            .text.strip()
        )

        if location.split(",")[-1].strip() in ["GB", "US"]:
            data.append(
                [
                    item.find_element(
                        By.CSS_SELECTOR, "span.section-title"
                    ).text.strip(),
                    com,
                    item.find_element(By.XPATH, ".//span[contains(text(), 'Location')]")
                    .find_element(By.XPATH, "./following-sibling::div")
                    .text.strip(),
                    link,
                ]
            )

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
