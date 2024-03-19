from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 113
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    try:
        driver.find_element(By.CSS_SELECTOR, "button#truste-consent-button").click()
    except Exception as e:
        print(f"Scraper{key} cookiee button: {e}")

    time.sleep(4)
    
    # driver.find_element(
    #     By.XPATH, "//button[contains(text(), 'Country/Region')]"
    # ).click()
    # driver.find_element(By.XPATH, "//span[contains(text(), 'United States')]").click()
    # driver.find_element(By.XPATH, "//span[contains(text(), 'United Kingdom')]").click()
    
    # time.sleep(40)

    # flag = True
    data = []

    # while flag:
    #     try:
    #         time.sleep(4)

    #         # items = driver.find_elements(
    #         #     By.CSS_SELECTOR, "a.JobListings_listing__qqquK"
    #         # )

    #         # for item in items:
    #         #     link = item.get_attribute("href").strip()
    #         #     location = item.find_element(
    #         #         By.CSS_SELECTOR, 'h4[data-testid="JobListings-location"]'
    #         #     ).text.strip()

    #         #     if location in ["United Kingdom", "United States"]:
    #         #         data.append(
    #         #             [
    #         #                 item.find_element(
    #         #                     By.CSS_SELECTOR, 'h3[data-testid="JobListings-title"]'
    #         #                 ).text.strip(),
    #         #                 com,
    #         #                 location,
    #         #                 link,
    #         #             ]
    #         #         )

    #         nextBtn = driver.find_element(By.CSS_SELECTOR, "a.next")

    #         if nextBtn.is_enabled():
    #             nextBtn.click()
    #         else:
    #             flag = False
    #     except:
    #         flag = False

    updateDB(key, data)


if __name__ == "__main__":
    main()
