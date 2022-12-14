from django.views.decorators.csrf import csrf_exempt
from auctionapp.models import User, Product, Bid
from django.shortcuts import get_object_or_404
from django.http import JsonResponse,  JsonResponse
import json
from django.core.mail import send_mail

def getWinner(request, product_id, timeleft):
    if request.method == "GET":
        if timeleft == 0:
            getproduct = Product.objects.get(id=product_id)
            winningBid = Bid.objects.filter(product=getproduct).get(winner=True) #filters the bids where id=product id, then gets the
            #one where winner is true
            user = winningBid.bidder #gets the user from that winning bid
            useremail = user.email #gets the users email
            return JsonResponse({
                'user_id': user.id,
                'user_email':useremail,
            },status=200)
        else:
            return JsonResponse({
                'user_id':0,
                'user_email':"",
            }, status=200)


def emailWinner(request, user_id, product_id, timeleft):
    if request.method == "GET":
        if timeleft == 0:
            user = get_object_or_404(User, id=user_id)
            product = get_object_or_404(Product, id=product_id)
            useremail = user.email
            productname = product.product_name
            productowner = product.owner.email
            send_mail(
            'Bid Winner',
            ('Hi, you have won '+productname+". Please contact "+productowner+" for more information."),
            'tams2022group8@gmail.com',
            [useremail],
            fail_silently=False,)
            return JsonResponse({
                'useremail':useremail
            })
        else:
            return JsonResponse({
                'useremail':""
            }, status=200)