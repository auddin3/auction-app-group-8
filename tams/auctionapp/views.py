from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse, HttpRequest, JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json

from auctionapp.models import User

def profile_api(request, user_id):

    user = get_object_or_404(User, id=user_id)

    if request.method == 'GET':
        return JsonResponse(user.to_dict(), status=200)