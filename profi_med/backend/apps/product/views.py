from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import json
from .models import SubCategory, Category, Product
# Create your views here.
from .models import SubCategory
from django.views.generic import ( ListView )


def get_subcategory(request):
    id = request.GET.get('id', '')
    result = list(SubCategory.objects.filter(
    category_id=int(id)).values('id', 'name'))
    return HttpResponse(json.dumps(result), content_type="application/json")

class IndexPage(ListView):
    template_name = "index.html"
    model = Product
    context_object_name = 'products'



class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    paginate_by = 99
    context_object_name = 'products'

