from threading import Thread
import importlib
from utils import updateDB, filterUrls, getBotSpeed

num_threads = getBotSpeed()

scraper_modules = [f"scripts.scraper{id}" for id in filterUrls()]


def scraping(scraper, name):
    try:
        scraper()
    except Exception as e:
        print(f"{name}: {e}")


def run():
    scrapers = [
        (importlib.import_module(module).main, module.split(".")[-1])
        for module in scraper_modules
    ]

    for i in range(0, len(scrapers), num_threads):
        threads = []

        for scraper, name in scrapers[i : i + num_threads]:
            thread = Thread(target=scraping, args=(scraper, name))
            threads.append(thread)
            thread.start()

        for thread in threads:
            thread.join()

        updateDB()


if __name__ == "__main__":
    run()
