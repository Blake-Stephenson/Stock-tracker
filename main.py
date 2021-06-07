__author__ = "Blake H. Stephenson"
__version__ = "0.0.3"

from stocks import StockBank
import urllib3
from bs4 import BeautifulSoup
from csv import DictReader, DictWriter



# ****************************************
# get list of currencies to be used
# ****************************************
# the reasons the UI is so inefficient is because it will be done using physical buttons on a microcontroller eventually
print("select the currencies you want to know the prices of")
print("q to add current currency, w to show next currency, e the finish")

# index of the currencies


cryptoList = StockBank()
cryptoList.add_file("cryptos.txt")
stockList = StockBank()

userList = StockBank()

#functions for crypto inputs
def Q():
    userList.add_stock(cryptoList.get())
    cryptoList.next()
    return 0


def W():
    cryptoList.next()
    return 0


def E():
    return 1

#switch for crypto selection
def button_decode(argument):
    switcher = {
        "q": Q,
        "w": W,
        "e": E
    }
    func = switcher.get(argument, lambda: "Invalid Input")
    return func()

#functions for stock inputs
def Qs():
    userList.add_stock(stockList.get())
    stockList.next()
    return 0


def Ws():
    stockList.next()
    return 0


def Es():
    return 1


def button_decode_stock(argument):
    #same as other switch but for stocks
    switcher = {
        "q": Qs,
        "w": Ws,
        "e": Es
    }
    func = switcher.get(argument, lambda: "Invalid Input")
    return func()

keyInput = 0
while keyInput != 1:
    keyInput = button_decode(input(cryptoList.get() + " q(add)/w(next)/e(exit)"))

# ****************************************
# scraping binance for requested data
# ****************************************

#array of prices to be used
prices = []
while True:
    for i in userList.get_bank():
        # All of the page URLs follow the same format with the exception of the ticker before "_USDT" is changed
        url = f'https://www.binance.com/en/trade/{i}_USDT?layout=pro&type=spot'

        # getting the html code from specified website
        req = urllib3.PoolManager()
        res = req.request('GET', url)
        soup = BeautifulSoup(res.data, 'html.parser')

        title = (soup.title.getText())
        prices.append(title.split(" | ")[0])

    # Combine both lists into a dictionary
    res = dict(zip(userList.get_bank(), prices))

    # Create an Excel Document with the dictionary
    with open("data.txt", 'w', newline='') as file:
        headers = ("Currency", 'Price (in USDT)')
        csv_writer = DictWriter(file, fieldnames=headers)
        csv_writer.writeheader()
        for k, v in res.items():
            csv_writer.writerow({
                'Currency': k,
                'Price (in USDT)': v
            })
    prices = []
