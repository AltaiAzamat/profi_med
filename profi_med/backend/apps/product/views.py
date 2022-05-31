from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import TemplateView
import json
from .models import SubCategory, Category, Product,BanerImage
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
    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     baners = BanerImage.objects.all()
    #     if len(baners) > 6:
    #         banners = baners[:6]
    #     context['baners'] = baners
    #     return context



class ProductListView(ListView):
    model = Product
    template_name = "product_list.html"
    paginate_by = 6
    context_object_name = 'products'





# def product(request):
#     products = Product.objects.all()
#     context = {
#         'produc' : products
#     }
#     return render(request,"index.html",context)