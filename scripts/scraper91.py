import requests
from bs4 import BeautifulSoup
from utils import readUrl, updateDB


def main():
    key = 91
    com, url = readUrl(key)
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")

    data = []

    items = soup.select("div.toptext")

    for item in items:
        link = item.select_one("a")["href"].strip()

        data.append(
            [
                item.select_one("h4.xs-heading").text.strip(),
                com,
                "UK",
                f"url{link}",
            ]
        )

    updateDB(key, data)


if __name__ == "__main__":
    main()
