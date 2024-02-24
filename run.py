from scripts.scraper1 import main as _1         


def run():
    try: _1() 
    except Exception as e: print(f'Scraper1: {e}')
    
    
if __name__ == "__main__":
    run()