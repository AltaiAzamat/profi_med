from django.urls import path
from .views import *
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('', IndexPage.as_view(), name='index'),
    path('specialist/', ProductListView.as_view(), name='product_list'),
    path('list/category/<slug:slug>/', ProductListView.as_view(), name="category_products"),
    path('list/category/<slug:slug>/<slug:subcategory_slug>/', ProductListView.as_view(), name="subcategory_products"),

    # path('new/', new, name = 'new')
    # path('getSubcategory/',product, name = "get_subcategory"),

]