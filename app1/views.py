from django.shortcuts import render
from django.http import HttpResponse,Http404,HttpResponseRedirect

# Create your views here.
def home(request):
    return render(request,"app1/home.html")

def about(request):
    return render(request,"app1/about.html")

def portfolio(request):
    return render(request,"app1/portfolio.html")

def view_market(request):
    return render(request,"app1/view_market.html")