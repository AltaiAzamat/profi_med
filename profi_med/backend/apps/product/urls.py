from django.urls import path
from .views import *
urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('specialist/', ProductListView.as_view(), name='product_list'),
    # path('getSubcategory/',product, name = "get_subcategory"),

]