from threading import Thread
from scripts.scraper1 import main as _1
from scripts.scraper2 import main as _2
from scripts.scraper3 import main as _3
from scripts.scraper4 import main as _4
from utils import updateDB

num = 2

def scraping(scraper, name):
    try:
        scraper()
    except Exception as e:
        print(f'{name}: {e}')

def run():
    scrapers = [
        (_1, 'Scraper1'), 
        (_2, 'Scraper2'), 
        (_3, 'Scraper3'), 
        (_4, 'Scraper4')
    ]
    
    threads = []

    for i in range(0, len(scrapers), num): 
        for scraper, name in scrapers[i:i+num]:
            thread = Thread(target=scraping, args=(scraper, name))
            
            threads.append(thread)
            
            thread.start()

        for thread in threads: 
            thread.join()
            
        threads = [] 
        
        updateDB()

if __name__ == "__main__":
    run()
    