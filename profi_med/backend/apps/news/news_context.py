from .models import *


def get_news(request):
    news = Articles.objects.all()
    return {'news': news}