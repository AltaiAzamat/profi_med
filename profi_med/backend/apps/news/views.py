from django.shortcuts import render
from django.shortcuts import render, redirect
from .models import *
from django.views.generic import ( ListView )


class NewsListView(ListView):
    model = Articles
    template_name = "news.html"
    paginate_by = 99
    context_object_name = 'news'