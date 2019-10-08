from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import path
from rainforest.models import Product, Review
from rainforest.forms import ProductForm, ReviewForm

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
  reviews = product.reviews.order_by("-published_date")
  review_form = ReviewForm()
  context = {
    'product': product,
    'title': product.name,
    'reviews': reviews,
    'form': review_form,
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


def review_create(request, product_id):
  product = Product.objects.get(id=product_id)
  form = ReviewForm(request.POST)
  if form.is_valid():
    review = form.instance
    review.product = product
    review.save()
    return redirect('product_show', product.id)
  else:
    reviews = product.reviews.order_by("-published_date")
    context = {
      'product': product,
      'form': form,
      'reviews': reviews,
      'title': 'Submit a Review',
    }
    response = render(request, 'products/product.html', context)
    return response
#-------------------------------


def review_edit(request, product_id, review_id):
  product = Product.objects.get(id=product_id)
  review = Review.objects.get(id=review_id)
  form = ReviewForm(instance=review)
  context = {
    'form': form,
    'title': 'Edit Review',
    'review': review,
    'product': product
  }
  response = render(request, 'reviews/edit.html', context)
  return HttpResponse(response)
#-------------------------------


def review_update(request, product_id, review_id):
  product = Product.objects.get(id=product_id)
  review = Review.objects.get(id=review_id)
  form = ReviewForm(request.POST, instance=review)
  if form.is_valid():
    form.save()
    return redirect('product_show', product.id)
  else:
    context = {
      'form': form,
      'title:': 'Edit Review',
      'product': product,
      'review': review,
    }
    response = render(request, 'reviews/edit.html', context)
    return HttpResponse(response)
#-------------------------------