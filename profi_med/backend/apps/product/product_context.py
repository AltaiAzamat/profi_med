from .models import *

def get_products(request):
    product = Product.objects.all()
    return {'product': product}