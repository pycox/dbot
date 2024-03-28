from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 146
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    availableLocations = ['United Kingdom', 'Gatwick']
    
    data = []

    for selectedLocation in availableLocations:
        try:
            time.sleep(4)
            driver.find_element(By.CSS_SELECTOR, "select#ctl00_ctl00_banner_TopSearch_LocationsList").click()
            time.sleep(2)
            driver.find_element(By.XPATH, "//option[contains(text(), '"+selectedLocation + "')]").click()
            time.sleep(4)
            driver.find_element(By.CSS_SELECTOR, "a#ctl00_ctl00_banner_TopSearch_btnSearch").click()
            time.sleep(4)
            
            flag = True
        
            while flag:
                try:
                    time.sleep(4)
                    
                    items = driver.find_elements(By.CSS_SELECTOR, "div.vsr-job")
                    
                    for item in items:
                        link = item.find_element(By.CSS_SELECTOR, "h3.vsr-job__title > a").get_attribute('href')
                        title = item.find_element(By.CSS_SELECTOR, "h3.vsr-job__title > a").text.strip()
                        location = item.find_element(By.CSS_SELECTOR, "div[data-id='div_content_VacV_LocationID'] > span").text.strip()
                        data.append([
                            title,
                            com,
                            location,
                            link
                        ])

                    try:
                        time.sleep(4)
                        driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                        time.sleep(4)
                        if len(driver.find_elements(By.CSS_SELECTOR, "input[name='epdsubmit']")) > 0:
                            driver.find_element(By.CSS_SELECTOR, "input[name='epdsubmit']").click()
                        
                        # nextBtn = WebDriverWait(driver, 10).until(
                        #     EC.element_to_be_clickable((By.XPATH, "//a[contains(text(), 'Next')]"))
                        # )


                        paginator = driver.find_element(By.CSS_SELECTOR, "div.paginator")
                        nextBtn = paginator.find_element(By.XPATH, "//a[contains(text(), 'Next')]")

                        print("Next BTN")

                        actions = ActionChains(driver)
                        actions.move_to_element(nextBtn)
                        actions.click(nextBtn)
                        actions.perform()

                        print("waiting")

                        # print(nextBtn)

                        
                        nextBtn.click()

                    except Exception as e:
                        print(e)
                        flag = False
                    
                except Exception as e:
                    flag = False

        except Exception as e:
            print(f"Scraper{key} cookiee button: {e}")

    print(len(data))
    return
    updateDB(key, data)

if __name__ == "__main__":
    main()
    