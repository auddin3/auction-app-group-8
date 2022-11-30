from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
#def index(request):
 #   return HttpResponse("Hello, world. You're at the auction app index.")

def login(request):
    return render(request, 'auctionapp/login.html')

def signup(request):
    return render(request, 'auctionapp/signup.html')