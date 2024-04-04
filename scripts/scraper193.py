from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
# from utils import readUrl, updateDB
import time


def main():
    key = 193
    com, url = "Uswitch", "https://www.rvu.co.uk/brands/uswitch"
    # com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    items = driver.find_elements(By.CSS_SELECTOR, "h3.css-153v4ra")

    data = []

    for index, item in enumerate(items):
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()
        location = item.find_element(By.CSS_SELECTOR, 'p.css-1v9gy2b:nth-child('+index+')').text.strip()
        print(location)

        for str in ['London', 'New York', 'San Francisco', 'United States', 'United Kingdom', 'UK', 'USA', 'US']:
            if (str in location):
                data.append(
                    [
                        item.find_element(By.CSS_SELECTOR, "a").text.strip(),
                        com,
                        location,
                        link,
                    ]
                )
                break

    driver.quit()
    print(data)
    # updateDB(key, data)


if __name__ == "__main__":
    main()
