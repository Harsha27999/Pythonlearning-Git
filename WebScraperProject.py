# import libraries 

from bs4 import BeautifulSoup
import requests
import time
import datetime

# Connect to Website and pull in data

URL = 'https://www.converseonlineindia.com/products/converse-chuck-taylor-all-star-leather-mens-sneakers-black-gh5462398-p-784.html'

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/78.0.3904.108 Safari/537.36", "Accept-Encoding":"gzip, deflate", "Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8", "DNT":"1","Connection":"close", "Upgrade-Insecure-Requests":"1"}

page = requests.get(URL, headers=headers)

soup1 = BeautifulSoup(page.content, "html.parser")

soup2 = BeautifulSoup(soup1.prettify(), "html.parser")

title = soup2.find(id='productName').get_text()

price = soup2.find(id='productPrices').get_text()


price = price.strip()[1:]
title = title.strip()

import datetime

today = datetime.date.today()
    
import csv 

header = ['Title', 'Price', 'Date']
data = [title, price, today]

with open('AmazonWebScraperDataset.csv', 'a+', newline='', encoding='UTF8') as f:
    writer = csv.writer(f)
    writer.writerow(data)
 
    


