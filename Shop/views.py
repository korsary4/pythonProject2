from django.shortcuts import render
from .models import Product
from django.views import View
from django.http import HttpResponse
from django.shortcuts import get_object_or_404

from .models import Product, Cart

# Create your views here.


class ProductViewAdd(View):
    def get(self, request):
   #     product = Product.objects.all()
   #     if 'type' in request.GET:
   #         product = product.filter(type=request.GET['type'])
        #print(product)
   #     return HttpResponse(product)
        params = request.GET
        product = Product(name=params['name'], type = params['type'])
        print(params)
        try:
            product.save()
        except Exception as error:
            return HttpResponse(f"Product {params['name']} create error !")
        return HttpResponse(f"Product {product.name} {product.get_type_display()}create successful!")




class ProductView(View):
    def get(self, request, pk):
       # product = Product.objects.get(pk = pk)
        product = get_object_or_404(Product, pk = pk)
        return HttpResponse(f"Product {product.name}, {product.get_type_display()}")

class ProductViewAll(View):
    def get(self, request):
        product = Product.objects.all()
        if 'type' in request.GET:
            product = product.filter(type=request.GET['type'])
       # print(product)
        return HttpResponse(product)

class CartView(View):
    def get(self, request):
        email = request.GET['email']
        cart = Cart.objects.filter(user__email=email).order_by('-create_at')
     #   user = request.GET['user']
     #   cart = Cart.objects.filter(pk=user)
        return HttpResponse(cart)