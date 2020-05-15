import pandas as pd

import canadaSoup
import mexicoSoup
import usaSoup

# Convert list from scraper to xlsx
def canToXLSX():
    canadaProvinces = canadaSoup.scrapeCanada()
    pd.DataFrame(canadaProvinces).to_excel('canadaSoup.xlsx')
    
def mexToXLSX():
    mexicoStates = mexicoSoup.scrapeMexico()
    pd.DataFrame(mexicoStates).to_excel('mexicoSoup.xlsx')

def usaToXLSX():
    usaStates = usaSoup.scrapeUSA()
    pd.DataFrame(usaStates).to_excel('usaSoup.xlsx')
    
if __name__ == "__main__":
    canToXLSX()
    mexToXLSX()
    usaToXLSX()

