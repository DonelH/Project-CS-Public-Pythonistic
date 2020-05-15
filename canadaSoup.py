import requests
from bs4 import BeautifulSoup
import re

url_data = 'https://www.canada.ca/en/public-health/services/diseases/2019-novel-coronavirus-infection.html?topic=tilelink'
page = requests.get(url_data)
canada_list = []

soup = BeautifulSoup(page.content, 'html.parser')
table = soup.find('table', class_ = 'table table-striped table-bordered table-hover')
prov_elems = table.find_all('tr')

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

if __name__ == '__main__':
    scrapeCanada()
                   

