from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 88
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    flag = True
    data = []

    while flag:
        try:
            time.sleep(4)

            items = driver.find_elements(By.CSS_SELECTOR, "div.result")

            for item in items:
                link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
                location = (
                    item.find_element(
                        By.XPATH, ".//strong[contains(text(), 'Location')]"
                    )
                    .find_element(By.XPATH, "..")
                    .text.strip()
                )
                
                if location.split(",")[-1].strip() in [
                    "United Kindom",
                    "United States",
                ]:
                    data.append(
                        [
                            item.find_element(
                                By.CSS_SELECTOR, "div.card-header"
                            ).text.strip(),
                            com,
                            location,
                            link,
                        ]
                    )

            nextBtn = driver.find_element(By.XPATH, "//a[contains(text(), '›')]")

            if nextBtn.is_enabled():
                nextBtn.click()
            else:
                flag = False
                break
        except Exception as e:
            # print(e)
            flag = False

    updateDB(key, data)


if __name__ == "__main__":
    main()
