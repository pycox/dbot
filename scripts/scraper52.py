import requests
from bs4 import BeautifulSoup
from utils import readUrl, updateDB


def main():
    key = 52
    com, url = readUrl(key)

    response = requests.get(url)

    soup = BeautifulSoup(response.text, "html.parser")

    items = soup.select("div.posting")

    data = []

    for item in items:
        link = item.find("a").get("href").strip()
        title = item.find("h5").text.strip()
        location = item.find_all("span")[-1].text.strip()

        data.append([title, com, location, link])

    updateDB(key, data)


if __name__ == "__main__":
    main()
