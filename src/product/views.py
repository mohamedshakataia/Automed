from django.shortcuts import render
from .models import jumia ,Category
from django.views.generic import ListView ,DetailView
from django.core.paginator import Paginator #import Paginator
# Create your views here.

class Product_List(ListView):
    model = jumia
    paginate_by = 50
    
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["cat"] =Category.objects.all() 
        return context

def filter_by_category(request,name_category):
    pro = jumia.objects.filter(category__sweetName=name_category)
    return render(request,'product/list.html',{'pro':pro})


class Product_Detail(DetailView):
    model = jumia


