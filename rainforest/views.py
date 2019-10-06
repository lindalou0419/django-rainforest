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
  response = render(request, 'products/new.html', context)
  return HttpResponse(response)
#-------------------------------


def product_create(request):
  form = ProductForm(request.POST)
  if form.is_valid():
    form.save()
    return redirect('products')
  else:
    context = {'form': form}
    return render(request, 'products/new.html', context)
#-------------------------------


def product_edit(request, product_id):
  product = Product.objects.get(id=product_id)
  form = ProductForm(instance=product)
  context = {
    'form': form,
    'title': f'Edit {product.name} Information',
    'product': product
  }
  response = render(request, 'products/edit.html', context)
  return HttpResponse(response)
#-------------------------------

def product_update(request, product_id):
  product = Product.objects.get(id=product_id)
  form = ProductForm(request.POST, instance=product)
  if form.is_valid():
    form.save()
    return redirect('product_show', product.id)
  else:
    context = {
      'form': form,
      'title': f'Edit {product.name} Information',
      'product': product,
    }
    response = render(request, 'products/edit.html', context)
    return HttpResponse(response)
#-------------------------------

def product_delete(request, product_id):
  product = Product.objects.get(id=product_id)
  product.delete()
  return redirect('products')
#-------------------------------