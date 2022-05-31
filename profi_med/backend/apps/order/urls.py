from django.urls import path
from .views import *
urlpatterns = [
    path('new/', new.as_view(), name='new'),
]