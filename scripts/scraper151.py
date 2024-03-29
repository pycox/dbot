from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time
from selenium_stealth import stealth
import random


def main():
    key = 151
    com, url = readUrl(key)
    options = Options()
    user_agents = [
        # Your list of user agents goes here
        "Mozilla/5.0 (Windows NT 10.0; Win64; x64)...",
        # More user agents
    ]
    user_agent = random.choice(user_agents)
    options.add_argument(f"user-agent={user_agent}")
    options.add_argument("--disable-blink-features=AutomationControlled")
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    stealth(
        driver,
        languages=["en-US", "en"],
        vendor="Google Inc.",
        platform="Win32",
        webgl_vendor="Intel Inc.",
        renderer="Intel Iris OpenGL Engine",
        fix_hairline=True,
    )
    driver.get(url)

    time.sleep(20)

    try:
        driver.find_element(
            By.CSS_SELECTOR, "button#onetrust-accept-btn-handler"
        ).click()
    except Exception as e:
        print(f"Scraper{key} cookie Button: {e}")

    data = []
    items = driver.find_elements(By.CSS_SELECTOR, "div.job")

    for item in items:
        link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href")
        location = item.find_element(By.CSS_SELECTOR, "div.job__location").text.strip()

        data.append(
            [
                item.find_element(By.CSS_SELECTOR, "div.job__title").text.strip(),
                com,
                location,
                link,
            ]
        )

    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
