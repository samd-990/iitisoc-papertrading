from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect
import time
from yahooquery import Ticker
from concurrent.futures import ThreadPoolExecutor

# Create your views here.
def home(request):
    return render(request,"app1/home.html")

def about(request):
    return render(request,"app1/about.html")

def portfolio(request):
    return render(request,"app1/portfolio.html")

def view_market(request):
    # price_list.clear()
    if len(price_list)==0:
        stock_data()
    price_list.sort(key= lambda x:x['cap'],reverse=True)
    return render(request,"app1/view_market.html",{
        "stock_info":price_list
    })


price_list=[]
def retrieve_data(ticker):
    price=float(Ticker(ticker).price[ticker].get('regularMarketPrice'))
    prevclose=float(Ticker(ticker).price[ticker].get('regularMarketPreviousClose'))
    change=price-prevclose
    changepercent=(change/prevclose)*100
    changedir=0
    if change<0:
        changedir=-1
    elif change>0:
        changedir=1
    price_list.append({
        "name":ticker,
        "price":"{:,.2f}".format(price),
        "cap":float(Ticker(ticker).price[ticker].get('marketCap')),
        "prevclose":prevclose,
        "changedir":changedir,
        "change":round(change,2),
        "changepercent":round(changepercent,2)
    })
    # print(f"{ticker} {Ticker(ticker).price[ticker].get('regularMarketPrice')}")

# def price(s):
#     for i in range()

# print("start")
# t0=time.time()
def stock_data():
    ticker_list=open('app1\stocks.txt','r').read().split('\n')
    with ThreadPoolExecutor(100) as executor:
        executor.map(retrieve_data, ticker_list)
# print(stock_data())
# print("end",time.time()-t0)