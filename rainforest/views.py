from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import path
from rainforest.models import Product
from rainforest.forms import ProductForm

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
  response = render(request, 'products/product.html', context)
  return HttpResponse(response)
#-------------------------------


def product_new(request):
  form = ProductForm()
  context = {'form': form}
  response = render(request, 'products/new-product.html', context)
  return HttpResponse(response)
#-------------------------------


def product_create(request):
  new_product = ProductForm(request.POST)
  if new_product.is_valid:
    new_product.save()
    return redirect('products')
  else:
    print(form)
#-------------------------------