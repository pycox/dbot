from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 182
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    items = driver.find_elements(By.CSS_SELECTOR, "select.selectGlobal.form-select > option")

    data = []

    for item in items:
        data.append(
            [
                item.text.strip(),
                com,
                "UK",
                "",
            ]
        )

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
