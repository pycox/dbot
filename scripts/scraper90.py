import requests
from bs4 import BeautifulSoup
from utils import readUrl, updateDB


def main():
    key = 90
    com, url = readUrl(key)
    response = requests.get(url)
    html_content = response.text

    soup = BeautifulSoup(html_content, "html.parser")

    data = []

    items = soup.select("li.job-result-item")

    for item in items:
        link = item.select_one("a")["href"].strip()

        data.append(
            [
                item.select_one("div.job-title").text.strip(),
                com,
                item.select_one("li.results-job-location").text.strip(),
                link,
            ]
        )

    updateDB(key, data)


if __name__ == "__main__":
    main()
