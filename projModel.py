# Model Portion of project by Code Scrappers. Major functions include the soups
# which scrape the websites for COVID-19 related information and news.

import requests
from bs4 import BeautifulSoup
import re
from urllib.request import urlopen

# BeautifulSoup setup for scraping of USA information regarding COVID-19.
# Specifies soup as necessary to gain access to required elements. Uses
# wikipedia as source.
usa_URL = 'https://en.wikipedia.org/wiki/COVID-19_pandemic_in_the_United_States'
page_USA = requests.get(usa_URL)
soup_USA = BeautifulSoup(page_USA.content, 'html.parser')
usa_results = soup_USA.find(id = 'mw-content-text')
usa_results_table = usa_results.find('table', class_ = 'wikitable')
usa_state_elems = usa_results_table.find_all('tr')
usa_state_list = []

# BeautifulSoup setup for scraping of Canada information regarding COVID-19.
# Specifies soup as necessary to gain access to required elements. Uses
# official Canada website as source.
can_URL = 'https://www.canada.ca/en/public-health/services/diseases/2019-novel-coronavirus-infection.html?topic=tilelink'
page_CAN = requests.get(can_URL)
soup_CAN = BeautifulSoup(page_CAN.content, 'html.parser')
can_table = soup_CAN.find('table', class_ = 'table table-striped table-bordered table-hover')
prov_elems = can_table.find_all('tr')
canada_list = []

# BeautifulSoup setup for scraping of Mexico information regarding COVID-19.
# Specifies soup as necessary to gain access to required elements. Uses
# wikipedia as source.
mex_URL = 'https://en.wikipedia.org/wiki/2020_coronavirus_pandemic_in_Mexico'
page_MEX = requests.get(mex_URL)
soup_MEX = BeautifulSoup(page_MEX.content, 'html.parser')
mex_results = soup_MEX.find(id = 'mw-content-text')
mex_results_table = mex_results.find('table', class_ = 'wikitable')
mex_state_elems = mex_results_table.find_all('tr')
mex_state_list = []

# BeautifulSoup setup for scraping of news articles regarding COVID-19. Uses
# google search engine as source.
news_URL = "https://news.google.com/rss/search?q=covid-19&hl=en-US&sort=date&gl=US&num=100&ceid=US:en"
Client = urlopen(news_URL)
xml_page = Client.read()
Client.close()
soup_page = BeautifulSoup(xml_page,"xml")
results = soup_page.findAll("item")
news_list = []

# Function which goes through html code provided by soup to make a sublist from
# relevant information (cases, deaths, and prov/state name) to append to country
# list. Also, function cleans out the information pulled of html, punctuation,
# and converting to int for cases/deaths. Specific to Canada website,
# specific code might differ than other scrapers due to different html. Returns
# country list containing sublists made on a per provice/state basis.
def scrapeCanada():
    canada_list.append(["Province Name", "Number of Cases", "Number of Deaths"])
    for prov_elem in prov_elems:
        td_list = prov_elem.find_all('td')
        if(td_list):
            prov_name = str(td_list[0])
            prov_name = prov_name[4:len(prov_name) - 5]
            prov_cases = re.sub('<|t|d|>|/|/|,', '', str(td_list[1]))
            prov_deaths = re.sub('<|t|d|>|/|,', '', str(td_list[3]))
            canada_list.append([prov_name, int(prov_cases), int(prov_deaths)])
    return canada_list

# Function which goes through html code provided by soup to make a sublist from
# relevant information (cases, deaths, and prov/state name) to append to country
# list. Also, function cleans out the information pulled of html, punctuation,
# and converting to int for cases/deaths. Specific to Mexico wiki page,
# specific code might differ than other scrapers due to different html. Returns
# country list containing sublists made on a per provice/state basis.
def scrapeMexico():
    mex_state_list.append(["State Name", "Number of Cases", "Number of Deaths"])
    for state_elem in mex_state_elems:
        if (state_elem.find('a') and state_elem.find('a').has_attr('title')):
            state_title = state_elem.find('a')['title']
            td_list = state_elem.find_all('td')
            state_cases = re.sub('<|t|d|>|/|,', '', str(td_list[0]))
            state_deaths = re.sub('<|t|d|>|/|,', '', str(td_list[2]))
            mex_state_list.append([state_title, int(state_cases),
                               int(state_deaths)])
    return mex_state_list

# Function which goes through html code provided by soup to make a sublist from
# relevant information (cases, deaths, and prov/state name) to append to country
# list. Also, function cleans out the information pulled of html, punctuation,
# and converting to int for cases/deaths. Specific to USA wiki page,
# specific code might differ than other scrapers due to different html. Returns
# country list containing sublists made on a per provice/state basis.
def scrapeUSA():
    usa_state_list.append(["State Name", "Number of Cases", "Number of Deaths"])
    for state_elem in usa_state_elems:
        if (state_elem.find('a') and state_elem.find('a').has_attr('title')
            and not(state_elem.has_attr('style'))):
            if(state_elem !=''):
                state_title = state_elem.find('a').text
                td_list = state_elem.find_all('td')
                state_cases = re.sub('<|t|d|>|/|,', '', str(td_list[0]))
                state_cases = state_cases.rstrip('\n')
                state_deaths = re.sub('<|t|d|>|/|,', '', str(td_list[1]))
                state_deaths = state_deaths.rstrip('\n')
                if(state_title == 'Kansas'):
                    state_cases = str(td_list[0])
                    state_cases = state_cases[4:9]
                    state_cases = re.sub('<|t|d|>|/|,', '', state_cases)
            usa_state_list.append([state_title, int(state_cases),
                                   int(state_deaths)])
    return usa_state_list

# Function which scrapes for news article in the google engine. It pulls only
# 5 articles from the engine and forms a sublist from each article with the
# relevant information. Returns the news list formed from these sublists.
def scrapeNews():
    counter = 0
    for news in results:
        if(counter < 5):
            news_list.append(news.title.text)
            news_list.append(news.link.text) 
            news_list.append(news.pubDate.text)
            counter +=1
    return news_list

if __name__ == '__main__':
    scrapeCanada()
    scrapeMexico()
    scrapeUSA()
    scrapeNews()
