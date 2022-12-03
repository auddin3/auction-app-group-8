from django.shortcuts import render
from auctionapp.forms import SignUpForm, LogInForm
from django.contrib import messages
from django.contrib.auth import authenticate, login

def login(request):
    form = LogInForm()
    if request.method == "POST":
        form = LogInForm(data=request.POST)
        uname = request.POST.get('username')
        pword = request.POST.get('password')
        user = authenticate(request, username=uname, password=pword)
        if user is not None:
            messages.success(request,'Log in worked')
            login(request,user)
        else:
            messages.error(request,'Login failed. Please try again')
    return render(request, 'auctionapp/login.html', {'form':form})

def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            form = SignUpForm()
            messages.success(request, 'Account created successfully')

    return render(request, 'auctionapp/signup.html', {'form': form})