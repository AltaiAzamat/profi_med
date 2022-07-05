from django.shortcuts import render, redirect
# from backend.apps.news.forms import ArticlesForm
# Create your views here.

def zapis(request):
    return render( request, 'zapis.html')