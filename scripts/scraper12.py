import requests
from bs4 import BeautifulSoup
from utils import readUrl, updateDB


def main():
    key = 12
    com, url = readUrl(key)
    
    response = requests.get(url)
    
    soup = BeautifulSoup(response.text, 'html.parser')
    
    items = soup.select('a.Card__StyledCard-sc-y213rf-1')
    
    data = []
    
    for item in items:
        link = item.get('href').strip()
        title = item.select_one("h3").text.strip() if item.select_one("h3") else ""
        location = "London" 
        
        data.append([title, com, location, link])
                
    updateDB(key, data)


if __name__ == "__main__":
    main()
