# Controller Portion for Project by the Code Scrappers. Major functions include
# the conversion from soups to excel and changing the map contained within the
# View.

import pandas as pd

import projModel
import projView

mexicoCovData = []
canadaCovData = []
usaCovData = []
newsSource = []

# Convert list from scraper to xlsx for Canada
def canToXLSX():
    canadaProvinces = projModel.scrapeCanada()
    for row in canadaProvinces:
        canadaCovData.append([row[0], row[1], row[2]])
    pd.DataFrame(canadaProvinces).to_excel('canadaSoup.xlsx')

def mexToXLSX():
    mexStates = projModel.scrapeMexico()
    for row in mexStates:
        mexicoCovData.append([row[0], row[1], row[2]])
    pd.DataFrame(mexStates).to_excel('mexicoSoup.xlsx')

def usaToXLSX():
    usaStates = projModel.scrapeUSA()
    for row in usaStates:
        usaCovData.append([row[0], row[1], row[2]])
    pd.DataFrame(usaStates).to_excel('usaSoup.xlsx')

def getNewsData():
    newsList = projModel.scrapeNews()
   
    newsStrOne = ''.join(newsList[0]) + ", " + ''.join(newsList[1]) + ", " +\
                 ''.join(newsList[2]) + "\n"
    newsStrTwo = ''.join(newsList[3]) + ", " + ''.join(newsList[4]) + ", " +\
                 ''.join(newsList[5]) + "\n"
    newsStrThree = ''.join(newsList[6]) + ", " + ''.join(newsList[7]) + ", " +\
                 ''.join(newsList[8]) + "\n"
    newsStrFour = ''.join(newsList[9]) + ", " + ''.join(newsList[10]) + ", " +\
                 ''.join(newsList[11]) + "\n"
    newsStrFive = ''.join(newsList[12]) + ", " + ''.join(newsList[13]) + ", " +\
                 ''.join(newsList[14])

    newsSource = "Trending News: \n" + "\n" +\
                 newsStrOne + "\n" +\
                 newsStrTwo + "\n" +\
                 newsStrThree + "\n" +\
                 newsStrFour + "\n" +\
                 newsStrFive 
    return newsSource

if __name__ == "__main__":
    canToXLSX()
    mexToXLSX()
    usaToXLSX()
    newsSource = getNewsData()
    projView.start(mexicoCovData, canadaCovData, usaCovData, newsSource)
