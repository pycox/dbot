from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from utils import readUrl, updateDB
import time


def main():
    key = 33
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    try:
        driver.find_element(By.CSS_SELECTOR, "a[href='/careers/jobs']").click()
    except Exception as e:
        print(f"Scraper{key} cookie Button: {e}")

    time.sleep(2)

    try:
        select = Select((driver.find_elements(By.CSS_SELECTOR, "select.select")[3]))
        select.select_by_value("gb")
    except Exception as e:
        print(f"Scraper{key} cookie Button: {e}")

    time.sleep(4)

    flag = True
    data = []

    while flag:
        try:
            time.sleep(4)

            items = driver.find_elements(By.CSS_SELECTOR, "app-button-job.job-link")

            for item in items:
                link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                title = item.find_element(By.CSS_SELECTOR, "h4.title").text.strip()
                location = item.find_elements(By.CSS_SELECTOR, "p")[1].text.strip()

                data.append([title, com, location, link])

            nextBtn = driver.find_element(By.CSS_SELECTOR, "button.next")

            if nextBtn.is_enabled():
                nextBtn.click()
            else:
                flag = False
        except:
            flag = False

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
