from auctionapp.forms import SignUpForm, LogInForm
from django.views.decorators.csrf import csrf_exempt
from django.contrib import messages
from django.contrib.auth import authenticate, login
from auctionapp.models import User, Product, Bid, FAQ
from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse, HttpResponseRedirect, JsonResponse, HttpResponseNotAllowed, HttpRequest
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
            ## return HttpResponseRedirect('http://127.0.0.1:5173')
            return HttpResponseRedirect('http://localhost:5173')
        else:
            messages.error(request,'Login failed. Please try again')
    return render(request, 'auctionapp/login.html', {'form':form})

def session_api(request : HttpRequest) -> JsonResponse:
    if request.method == "GET":
        return JsonResponse( { 'user_id' : request.session.__getitem__("_auth_user_id") } , safe=False )


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
            ],
        }, status=200)

@csrf_exempt
def product_details(request, product_id):
    if request.method == 'GET':
        reqProduct = Product.objects.get(id=product_id)

        return JsonResponse({
            'product': reqProduct.to_dict()
        }, status=200)

@csrf_exempt 
def comment_api(request, product_id):
    if request.method == 'GET':
        return JsonResponse({
            'comments': [
                question.to_dict()
                for question in FAQ.objects.filter(product=product_id)
            ],
        }, status=200)

    if request.method == 'POST':
        comment_details = json.loads(request.body)

        newProduct = Product.objects.get(id = product_id)
        newSender = User.objects.get(id=comment_details["sender"])
        defaultRecipient = User.objects.get(id=newProduct.owner.id)

        new_entry = FAQ.objects.create(product=newProduct, 
        recipient = defaultRecipient,
        sender = newSender,
        )

        new_entry.question = comment_details["question"]
        new_entry.answer = comment_details["answer"]
        new_entry.save()

        return JsonResponse({
            "comment": new_entry.to_dict(),
        }, status=200)

    if request.method == "PUT":
        comment_details = json.loads(request.body)

        comment = FAQ.objects.get(question = comment_details["question"])
        recip = User.objects.get(id = comment_details["recipient"])
        comment.answer = comment_details["answer"]
        comment.recipient = recip
        comment.save()
        
        return JsonResponse({
            "comment": comment.to_dict()
        }, status=200)

@csrf_exempt 
def bid_api(request, product_id):
    if request.method == 'POST':
        bid_details = json.loads(request.body)

        newProduct = Product.objects.get(id=product_id)
        newBidder = User.objects.get(id=bid_details["bidder"])

        new_entry = Bid.objects.create(bid_price = bid_details["bid_price"],
        product = newProduct,
        bidder = newBidder,
        winner = False,
        )
    
        new_entry.end_of_bid = newProduct.end_of_bid
        new_entry.is_active = True
        
        new_entry.save()

        try: 
            if Bid.objects.filter(product = newProduct).count() > 0:
                currentWinningBid = Bid.objects.get(winner=True)
                if currentWinningBid.bid_price < new_entry.bid_price:
                    currentWinningBid.winner = False
                    new_entry.winner = True
                    new_entry.save()
                    currentWinningBid.save()
        except:
            new_entry.winner = True
            new_entry.save()

        return JsonResponse({
            "Bid": new_entry.to_dict(),
        }, status=200)

def bidCount(request, product_id):
    if request.method == "GET":
         newProduct = Product.objects.get(id=product_id)
         winner = Bid.objects.get(winner=True)

    return JsonResponse({
        "total": Bid.objects.filter(product=newProduct).count(),
        "win": winner.bid_price,
    }, status=200)