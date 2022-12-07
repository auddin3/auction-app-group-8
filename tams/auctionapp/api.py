import json
from django.db.models import Q
from django.http import JsonResponse
from .models import Product

def api_search(request):
    products_list = []
    data = json.loads(request.body)
    query = data['query']

    products = Product.objects.filter(status=Product.ACTIVE).filter(Q(product_name__icontains=query) | Q(description__icontains=query))
    
    for product in products:
        obj = {
            'id': product.id,
            'product_name': product.product_name,
            ## 'product_image': product.product_image,
            'description': product.description,
            # 'start_price': product.start_price,
            # 'is_active': product.is_active,
            # 'owner': product.owner
            # 'url': '/products/%s/' % product.id
        }
        products_list.append(obj)
        print(obj)
    
    return JsonResponse({'products': products_list})