from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import Select
from utils import readUrl, updateDB
import time


def main():
    key = 251
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)

    try:
      select = Select(driver.find_element(By.CSS_SELECTOR, "div.perpage-select > select"))
      select.select_by_visible_text("100")
    except:
      print("No Select working")

    time.sleep(4)

    items = driver.find_elements(By.CSS_SELECTOR, "table.ats_list > tbody > tr")
    data = []

    for item in items:
        link = item.get_attribute("onclick").strip().replace("window.location.href=", "").replace("'", "")
        link = "https://ryman.ats.emea1.fourth.com" + link
          
        data.append(
            [
                item.find_element(By.CSS_SELECTOR, "td:first-child").text.strip(),
                com,
                "UK",
                link,
            ]
        )
    
    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
