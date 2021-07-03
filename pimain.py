__author__ = "Blake H. Stephenson"
__version__ = "1.0.0"

from stocks import StockBank
import urllib3
from bs4 import BeautifulSoup
import time
import RPi.GPIO as GPIO




#set up buttons
GPIO.setwarnings(False) #ignore warnings
GPIO.setmode(GPIO.BOARD)
GPIO.setup(29, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(31, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
GPIO.setup(33, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)


#Set up for lcd
#lcd code from tutorials-raspberrypi
#pins used
LCD_RS = 7
LCD_E  = 11
LCD_DATA4 = 12
LCD_DATA5 = 15
LCD_DATA6 = 16
LCD_DATA7 = 18

LCD_WIDTH = 16 		#line width
LCD_LINE_1 = 0x80 	#adress of line 1
LCD_LINE_2 = 0xC0 	#adress of line 2
LCD_CHR = GPIO.HIGH
LCD_CMD = GPIO.LOW
E_PULSE = 0.0005
E_DELAY = 0.0005

def lcd_send_byte(bits, mode):
	#set pins low
	GPIO.output(LCD_RS, mode)
	GPIO.output(LCD_DATA4, GPIO.LOW)
	GPIO.output(LCD_DATA5, GPIO.LOW)
	GPIO.output(LCD_DATA6, GPIO.LOW)
	GPIO.output(LCD_DATA7, GPIO.LOW)
	if bits & 0x10 == 0x10:
	  GPIO.output(LCD_DATA4, GPIO.HIGH)
	if bits & 0x20 == 0x20:
	  GPIO.output(LCD_DATA5, GPIO.HIGH)
	if bits & 0x40 == 0x40:
	  GPIO.output(LCD_DATA6, GPIO.HIGH)
	if bits & 0x80 == 0x80:
	  GPIO.output(LCD_DATA7, GPIO.HIGH)
	time.sleep(E_DELAY)    
	GPIO.output(LCD_E, GPIO.HIGH)  
	time.sleep(E_PULSE)
	GPIO.output(LCD_E, GPIO.LOW)  
	time.sleep(E_DELAY)      
	GPIO.output(LCD_DATA4, GPIO.LOW)
	GPIO.output(LCD_DATA5, GPIO.LOW)
	GPIO.output(LCD_DATA6, GPIO.LOW)
	GPIO.output(LCD_DATA7, GPIO.LOW)
	if bits&0x01==0x01:
	  GPIO.output(LCD_DATA4, GPIO.HIGH)
	if bits&0x02==0x02:
	  GPIO.output(LCD_DATA5, GPIO.HIGH)
	if bits&0x04==0x04:
	  GPIO.output(LCD_DATA6, GPIO.HIGH)
	if bits&0x08==0x08:
	  GPIO.output(LCD_DATA7, GPIO.HIGH)
	time.sleep(E_DELAY)    
	GPIO.output(LCD_E, GPIO.HIGH)  
	time.sleep(E_PULSE)
	GPIO.output(LCD_E, GPIO.LOW)  
	time.sleep(E_DELAY)  

def display_init():
	lcd_send_byte(0x33, LCD_CMD)
	lcd_send_byte(0x32, LCD_CMD)
	lcd_send_byte(0x28, LCD_CMD)
	lcd_send_byte(0x0C, LCD_CMD)  
	lcd_send_byte(0x06, LCD_CMD)
	lcd_send_byte(0x01, LCD_CMD)  

def lcd_message(message):
	message = message.ljust(LCD_WIDTH," ")  
	for i in range(LCD_WIDTH):
	  lcd_send_byte(ord(message[i]),LCD_CHR)
	
if __name__ == '__main__':
	GPIO.setwarnings(False)
	GPIO.setup(LCD_E, GPIO.OUT)
	GPIO.setup(LCD_RS, GPIO.OUT)
	GPIO.setup(LCD_DATA4, GPIO.OUT)
	GPIO.setup(LCD_DATA5, GPIO.OUT)
	GPIO.setup(LCD_DATA6, GPIO.OUT)
	GPIO.setup(LCD_DATA7, GPIO.OUT)
	display_init()


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
        'q': Q,
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

#lcd print instructions
lcd_send_byte(LCD_LINE_1, LCD_CMD)
lcd_message('select tickers')
time.sleep(2)
lcd_send_byte(LCD_LINE_1, LCD_CMD)
lcd_message('add next exit')

lcd_send_byte(LCD_LINE_2, LCD_CMD)

keyInput = 0
print(cryptoList.get()+" q(add)/w(next)/e(exit)")
#set cursor for tickers
lcd_send_byte(LCD_LINE_2, LCD_CMD)
lcd_message(cryptoList.get())
while keyInput != 1:
    if GPIO.input(29) == GPIO.HIGH:
        time.sleep(0.5)
        keyInput = button_decode('q')
        print(cryptoList.get()+" q(add)/w(next)/e(exit)")
        lcd_send_byte(LCD_LINE_2, LCD_CMD)
        lcd_message(cryptoList.get())
    if GPIO.input(31) == GPIO.HIGH:
        time.sleep(0.5)
        keyInput = button_decode('w')
        print(cryptoList.get()+" q(add)/w(next)/e(exit)")
        lcd_send_byte(LCD_LINE_2, LCD_CMD)
        lcd_message(cryptoList.get())
    if GPIO.input(33) == GPIO.HIGH:
        time.sleep(0.5)
        keyInput = button_decode('e')
    
keyInput = 0
print(stockList.get() + " q(add)/w(next)/e(exit)")
#set cursor for tickers
lcd_send_byte(LCD_LINE_2, LCD_CMD)
lcd_message(stockList.get())
while keyInput != 1:
    if GPIO.input(29) == GPIO.HIGH:
        time.sleep(0.5)
        keyInput = button_decode_stock('q')
        print(stockList.get() + " q(add)/w(next)/e(exit)")
        lcd_send_byte(LCD_LINE_2, LCD_CMD)
        lcd_message(stockList.get())
    if GPIO.input(31) == GPIO.HIGH:
        time.sleep(0.5)
        keyInput = button_decode_stock('w')
        print(stockList.get() + " q(add)/w(next)/e(exit)")
        lcd_send_byte(LCD_LINE_2, LCD_CMD)
        lcd_message(stockList.get())
    if GPIO.input(33) == GPIO.HIGH:
        time.sleep(0.5)
        keyInput = button_decode_stock('e')

# ****************************************
# scraping binance for requested data
# ****************************************


while True:
    # array of prices to be used
    prices = []
    for i in userList_c.get_bank():
        # All of the page URLs follow the same format with the exception of the ticker before "_USDT" is changed
        url = 'https://www.binance.com/en/trade/%s_USDT?layout=pro&type=spot' % i

        # getting the html code from specified website
        req = urllib3.PoolManager()
        res = req.request('GET', url)
        soup = BeautifulSoup(res.data, 'html.parser')

        title = (soup.title.getText())
        prices.append(title.split(" ")[0])


    # Combine both lists into a dictionary
    data = dict(zip(userList_c.get_bank(), prices))

    #print crypto data to word file
    f = open("data.txt", "w")

    f.write("Crypto, Price (in USDT)\n")
    #lcd print title
    lcd_send_byte(LCD_LINE_1, LCD_CMD)
    lcd_message('Crypto prices')
    for i in data:
        f.write(i+": "+data[i]+"\n")
        #lcd print prices
        lcd_send_byte(LCD_LINE_2, LCD_CMD)
	lcd_message(i+": "+data[i])
	time.sleep(0.5)
    f.close()

    prices = []
    for i in userList_s.get_bank():
        # All of the page URLs follow the same format with the exception of the ticker at the end to it is changed
        url = 'https://www.marketwatch.com/investing/stock/%s' % i

        # getting the html code from specified website
        req = urllib3.PoolManager()
        res = req.request('GET', url)
        soup = BeautifulSoup(res.data, 'html.parser')

        prices.append(soup.find(class_ = 'table__cell u-semi').getText())

    # Combine both lists into a dictionary
    data = dict(zip(userList_s.get_bank(), prices))

    #print stock data to word file
    f = open("data.txt", "a")
    f.write("Stock, Price (in USD)\n")
    #lcd print title
    lcd_send_byte(LCD_LINE_1, LCD_CMD)
    lcd_message('Stock prices')
    for i in data:
        f.write(i+": "+data[i]+"\n")
        #lcd print prices
        lcd_send_byte(LCD_LINE_2, LCD_CMD)
	lcd_message(i+": "+data[i])
	time.sleep(0.5)
    f.close()

    print("updated")
    time.sleep(5)

