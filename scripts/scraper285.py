from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 285
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)


    data = []
    flag = True

    total_page = driver.find_element(By.CSS_SELECTOR, "span.pagination-total-pages").text.strip()
    total_page = int(total_page.split("of")[1].strip())

    while flag:
        time.sleep(4)
        items = driver.find_elements(By.CSS_SELECTOR, "ul.search-results-list > li")
        for item in items:
            link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()
            location = item.find_element(By.CSS_SELECTOR, 'span.job-location').text.strip()

            for str in ['London', 'New York', 'San Francisco', 'United States', 'United Kingdom', 'UK', 'USA', 'US']:
                if (str in location):
                    data.append(
                        [
                            item.find_element(By.CSS_SELECTOR, "h2").text.strip(),
                            com,
                            location,
                            link,
                        ]
                    )
                    break
        
        try:
          button = driver.find_element(By.CSS_SELECTOR, "a.next")
          if button and total_page > 0:
            driver.execute_script("arguments[0].click();", button)
          else:
            flag = False
          total_page -= 1
        except:
          flag = False
          print("No More Jobs")

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
