# from scripts.scraper1 import main as _1         
from scripts.scraper2 import main as _2       


def run():
    # try: _1() 
    # except Exception as e: print(f'Scraper1: {e}')
    
    try: _2() 
    except Exception as e: print(f'Scraper2: {e}')
    
    
if __name__ == "__main__":
    run()