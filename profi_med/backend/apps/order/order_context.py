from .models import *

def get_order(request):
    zapis = Zapis.objects.all()
    return {'zapis': zapis}