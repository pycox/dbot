from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 48
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    try:
        driver.find_element(By.CSS_SELECTOR, "a#hs-eu-confirmation-button").click()
    except Exception as e:
        print(f"Scraper{key} cookiee button: {e}")

    time.sleep(4)

    data = []
    flag = True

    while flag:
        try:
            time.sleep(4)

            driver.find_element(By.CSS_SELECTOR, "button[rel='next']").click()

        except Exception as e:
            flag = False
            break

    items = driver.find_elements(By.CSS_SELECTOR, "li.whr-item")

    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()
        title = item.find_element(By.CSS_SELECTOR, "h3.whr-title").text.strip()
        locations = item.find_elements(By.CSS_SELECTOR, "li.whr-location")

        if len(locations) > 0:
            if locations[0].text.strip() in [
                "London",
                "Manchester",
                "Manchester",
                "Birmingham",
            ]:
                data.append(
                    [
                        title,
                        com,
                        locations[0].text.strip(),
                        link,
                    ]
                )

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
