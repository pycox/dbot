from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 61
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)
    try:
        driver.find_element(By.XPATH, "//button[contains(text(), 'Accept')]").click()
    except Exception as e:
        print(f"Scraper{key} cookie Button: {e}")
        
    time.sleep(4)

    flag = True
    data = []

    updateDB(key, data)


if __name__ == "__main__":
    main()
