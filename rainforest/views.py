# from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import path
from rainforest.models import Product

def root(request):
  return redirect('products')

def products(request):
  context = {
    'products': Product.objects.all(),
    'title': 'Django Rainforest',
  }
  response = render(request, 'index.html', context)
  return HttpResponse(response)