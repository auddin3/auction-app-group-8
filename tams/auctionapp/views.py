from auctionapp.forms import SignUpForm, LogInForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate, login
from auctionapp.models import User, Product, Bid
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotAllowed
import json

def loginUser(request):
    form = LogInForm()
    if request.method == "POST":
        form = LogInForm(data=request.POST)
        uname = request.POST.get('email')
        pword = request.POST.get('password')
        user = authenticate(request, username=uname, password=pword)
        if user is not None:
            login(request,user)
            return HttpResponseRedirect('http://localhost:5173')
        else:
            messages.error(request,'Login failed. Please try again')
    return render(request, 'auctionapp/login.html', {'form':form})

def signup(request):
    form = SignUpForm()
    if request.method == "POST":
        form = SignUpForm(request.POST)
        email=request.POST.get('email')
        username=request.POST.get('username')
        first_name=request.POST.get('first_name')
        last_name=request.POST.get('last_name')
        password=request.POST.get('password')
        if form.is_valid():
            user = User.objects.create_user(email,username,first_name,last_name,password)
            user.save()
            form = SignUpForm()
            messages.success(request, 'Account created successfully')

    return render(request, 'auctionapp/signup.html', {'form': form})

@csrf_exempt
def profile_api(request, user_id):

    user = get_object_or_404(User, id=user_id)

    # user = request.user

    if request.method == 'GET':
        items = Product.objects.filter(owner=user).count()
        bids = Bid.objects.filter(bidder=user).count()


        return JsonResponse({
            'user': user.to_dict(),
            'items': items,
            'bids': bids,
        }, status=200)

    elif request.method == 'PUT':
        payload = json.loads(request.body)

        user.first_name=payload["fname"]
        user.last_name=payload["lname"]
        user.email=payload["email"]
        user.date_of_birth=payload["dob"]

        user.save()

        if payload["username"] != user.username:
            try :
                username_exists = User.objects.get(username=payload["username"])
                if username_exists:
                    return HttpResponseNotAllowed("no")
            except User.DoesNotExist:
                user.username=payload["username"]
                user.save()
       
      
        return JsonResponse(user.to_dict(), status=200)

def fetch_products(request):
    if request.method == 'GET':
        return JsonResponse({
            'products': [
                product.to_dict()
                for product in Product.objects.all()
            ]
        })
