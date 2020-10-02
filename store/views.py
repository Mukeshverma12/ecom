from django.shortcuts import render,get_object_or_404
from django.views.generic import ListView, DetailView

from .models import Product,OrderItem,Order


# Create your views here.
class Store(ListView):
    model = Product
    template_name = 'store/Home.html'

class Product(DetailView):
    model = Product
    template_name = 'store/product.html'

def signup(request):
    return render(request,'store/Signup.html',{})

def add_to_cart(request,slug):
    product=get_object_or_404(Product,slug)
    order=OrderItem.objects.create(product=product)
    order_item=Order.objects.filter(user=request.user,order_item=False)

def search(request):
    query=request.GET['query']
    p=Product.objects.filter(title__icontainer=query)
    return render(request,'store/templates/search.html',{'p':p})
