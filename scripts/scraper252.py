from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 252
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    countries = driver.find_elements(By.CSS_SELECTOR, "div.positions--country")
    data = []

    for country in countries:
        country_name = country.find_element(By.CSS_SELECTOR, "h2").text.strip()
        if country_name in ['London', 'New York', 'San Francisco', 'United States', 'United Kingdom', 'UK', 'USA', 'US']:

            items = country.find_elements(By.CSS_SELECTOR, "div.positions-items > div.positions--card")
            for item in items:
                link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()

                data.append(
                    [
                        item.find_element(By.CSS_SELECTOR, "a").text.strip(),
                        com,
                        country_name,
                        link,
                    ]
                )

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
