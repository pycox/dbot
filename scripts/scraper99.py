import requests
from bs4 import BeautifulSoup
from utils import readUrl, updateDB


def main():
    key = 99
    com, url = readUrl(key)
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")

    data = []

    items = soup.select("div.opening")

    for item in items:
        link = item.select_one("a")["href"].strip()

        data.append(
            [
                item.select_one("a").text.strip(),
                com,
                item.select_one("span.location").text.strip(),
                f"url{link}",
            ]
        )

    updateDB(key, data)


if __name__ == "__main__":
    main()
