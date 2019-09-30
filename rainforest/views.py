# from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import path
from rainforest.models import Product

def root(request):
  return redirect('products')
#-------------------------------


def products(request):
  context = {
    'products': Product.objects.all(),
    'title': 'Django Rainforest',
  }
  response = render(request, 'index.html', context)
  return HttpResponse(response)
#-------------------------------


def product_show(request, product_id):
  product = Product.objects.get(id=product_id)
  context = {
    'product': product,
    'title': product.name,
  }
  response = render(request, 'product.html', context)
  return HttpResponse(response)
#-------------------------------