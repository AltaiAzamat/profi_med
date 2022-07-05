from django.urls import path
from .views import *


urlpatterns = [
    path('news/', NewsListView.as_view(), name='news'),

]