from django.shortcuts import render
from django.http import HttpResponse
from auctionapp.forms import SignUpForm, LogInForm
from django.contrib import messages



def login(request):
    form = LogInForm()
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