from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from utils import readUrl, updateDB
import time


def main():
    key = 211
    com, url = readUrl(key)
    options = Options()
    options.add_argument("--log-level=3")
    driver = webdriver.Chrome(options=options)
    driver.get(url)

    time.sleep(4)
    data = []

    total_jobs = driver.find_element(By.CSS_SELECTOR, 'span.paginationLabel').text.strip()
    total_jobs = total_jobs.split("of")[1].strip()
    
    current_jobs = 25
    while current_jobs < int(total_jobs):
      items = driver.find_elements(By.CSS_SELECTOR, "tr.data-row")
      
      for item in items:
          link = item.find_element(By.CSS_SELECTOR, "a").get_attribute("href").strip()
          location = item.find_element(By.CSS_SELECTOR, 'span.jobLocation').text.strip()

          for str in ['London', 'New York', 'San Francisco', 'United States', 'United Kingdom', 'UK', 'USA', 'US', 'GB']:
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
        
      current_jobs += 25
      if current_jobs < int(total_jobs):
        driver.get(url.split("?")[0] + "?q=&sortColumn=referencedate&sortDirection=desc&startrow="+str(current_jobs))
        time.sleep(4)


    driver.quit()

    updateDB(key, data)


if __name__ == "__main__":
    main()
