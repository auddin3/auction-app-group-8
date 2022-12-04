from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from auctionapp.models import User, Product, Bid

def profile_api(request, user_id):

    user = get_object_or_404(User, id=user_id)

    if request.method == 'GET':
        items = Product.objects.filter(owner=user).count()
        bids = Bid.objects.filter(bidder=user).count()


        return JsonResponse({
            'user': user.to_dict(),
            'items': items,
            'bids': bids,
        }, status=200)