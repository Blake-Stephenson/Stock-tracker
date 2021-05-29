__author__ = "Blake H. Stephenson"
__version__ = "0.0.0"

import urllib3, re
from bs4 import BeautifulSoup
from csv import DictReader, DictWriter

#currencies to be used
currencies = ["BTC","ETH","AVA"]
prices = []



#****************************************
#scraping binance for requested data
#****************************************
for i in currencies:
    # All of the page URLs follow the same format with the exception of the ticker before "_USDT" is changed
    url = f'https://www.binance.com/en/trade/{i}_USDT?layout=pro&type=spot'

    # getting the html code from specified website
    req = urllib3.PoolManager()
    res = req.request('GET', url)
    soup = BeautifulSoup(res.data, 'html.parser')

    title = (soup.title.getText())
    prices.append(title.split(" | ")[0])



# Combine both lists into a dictionary
res = dict(zip(currencies,prices))

#print(res)


# Create an Excel Document with the dictionary
with open("data", 'w', newline='') as file:
    headers = ("Currency", 'Price (in USDT)')
    csv_writer = DictWriter(file, fieldnames=headers)
    csv_writer.writeheader()
    for k, v in res.items():
        csv_writer.writerow({
            'Currency': k,
            'Price (in USDT)': v
        })