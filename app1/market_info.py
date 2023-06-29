import time
from yahooquery import Ticker
import yfinance as yf
from concurrent.futures import ThreadPoolExecutor

ticker_list=open('app1\stocks.txt','r').read().split('\n')
price_dict={}

# for i in yf.Ticker("INFY").info:
#     print(i)

print(yf.Ticker("INFY").info)

def retrieve_data(ticker):
    price_dict[ticker]=Ticker(ticker).price[ticker].get('regularMarketPrice')
    # print(f"{ticker} {Ticker(ticker).price[ticker].get('regularMarketPrice')}")

# print("start")
# t0=time.time()
def stock_data():
    with ThreadPoolExecutor(100) as executor:
        executor.map(retrieve_data, ticker_list)
    return price_dict
# print(stock_data())
# print("end",time.time()-t0)
