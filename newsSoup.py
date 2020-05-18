import bs4
import csv
from bs4 import BeautifulSoup as soup
from urllib.request import urlopen

news_url = "https://news.google.com/rss/search?q=covid-19&hl=en-US&sort=date&gl=US&num=100&ceid=US:en"
Client = urlopen(news_url)
xml_page = Client.read()
Client.close()

soup_page = soup(xml_page,"xml")
results = soup_page.findAll("item")

# Print news title, url and publish date
news_list = []

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
    scrapeNews()

