import requests
from bs4 import BeautifulSoup
from utils import readUrl, updateDB


def main():
    key = 71
    com, url = readUrl(key)

    response = requests.get(url)
    soup = BeautifulSoup(response.content, "html.parser")

    data = []

    items = soup.select("div.card-grid-container_cards > div")

    for item in items:
        link_tag = item.select_one("a")
        if link_tag:
            link = link_tag.get("href")

        location_tag = item.find("span", string=lambda text: "Location" in text)
        location = (
            location_tag.find_next_sibling("span").text.strip() if location_tag else ""
        )

        title_tag = item.select_one("h4")
        
        if title_tag:
            title = title_tag.text.strip()

        data.append([title, com, location, link])

    updateDB(key, data)


if __name__ == "__main__":
    main()
