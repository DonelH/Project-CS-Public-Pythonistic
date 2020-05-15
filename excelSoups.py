import pandas as pd

import mexicoSoup
import canadaSoup

# Convert list from scraper to xlsx
def mexToXLSX():
    mexicoStates = mexicoSoup.scrapeMexico()
    pd.DataFrame(mexicoStates).to_excel('mexicoSoup.xlsx')

def canToXLSX():
    canadaStates = canadaSoup.scrapeCanada()
    pd.DataFrame(canadaStates).to_excel('canadaSoup.xlsx')
    
if __name__ == "__main__":
    mexToXLSX()
    canToXLSX()
