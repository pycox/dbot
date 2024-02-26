# from scripts.scraper1 import main as _1         
# from scripts.scraper2 import main as _2       
# from scripts.scraper3 import main as _3       
# from scripts.scraper4 import main as _4       
from scripts.scraper5 import main as _5       


def run():
    # try: _1() 
    # except Exception as e: print(f'Scraper1: {e}')
    
    # try: _2() 
    # except Exception as e: print(f'Scraper2: {e}')
    
    # try: _3() 
    # except Exception as e: print(f'Scraper3: {e}')
    
    # try: _4() 
    # except Exception as e: print(f'Scraper4: {e}')
    
    try: _5() 
    except Exception as e: print(f'Scraper5: {e}')
    
    
if __name__ == "__main__":
    run()