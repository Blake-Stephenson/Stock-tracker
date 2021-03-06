__author__ = "Blake H. Stephenson"
__version__ = "0.0.4"

from stocks import StockBank
import urllib3
from bs4 import BeautifulSoup
import time


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
stockList.add_file("stocks.txt")

userList_c = StockBank()
userList_s = StockBank()

#functions for crypto inputs
def Q():
    userList_c.add_stock(cryptoList.get())
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
    userList_s.add_stock(stockList.get())
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
keyInput = 0
while keyInput != 1:
    keyInput = button_decode_stock(input(stockList.get() + " q(add)/w(next)/e(exit)"))


# ****************************************
# scraping binance for requested data
# ****************************************


while True:
    # array of prices to be used
    prices = []
    for i in userList_c.get_bank():
        # All of the page URLs follow the same format with the exception of the ticker before "_USDT" is changed
        url = f'https://www.binance.com/en/trade/{i}_USDT?layout=pro&type=spot'

        # getting the html code from specified website
        req = urllib3.PoolManager()
        res = req.request('GET', url)
        soup = BeautifulSoup(res.data, 'html.parser')

        title = (soup.title.getText())
        prices.append(title.split(" | ")[0])


    # Combine both lists into a dictionary
    data = dict(zip(userList_c.get_bank(), prices))

    #print crypto data to word file
    f = open("data.txt", "w")

    f.write("Crypto, Price (in USDT)\n")
    for i in data:
        f.write(i+": "+data[i]+"\n")
    f.close()

    prices = []
    for i in userList_s.get_bank():
        # All of the page URLs follow the same format with the exception of the ticker at the end to it is changed
        url = f'https://ca.finance.yahoo.com/quote/{i}?p={i}'

        # getting the html code from specified website
        req = urllib3.PoolManager()
        res = req.request('GET', url)
        soup = BeautifulSoup(res.data, 'html.parser')

        prices.append(soup.find("span",class_ = "Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)").getText())

    # Combine both lists into a dictionary
    data = dict(zip(userList_s.get_bank(), prices))

    #print stock data to word file
    f = open("data.txt", "a")
    f.write("Stock, Price (in USD)\n")
    for i in data:
        f.write(i+": "+data[i]+"\n")
    f.close()

    print("updated")
    time.sleep(5)

