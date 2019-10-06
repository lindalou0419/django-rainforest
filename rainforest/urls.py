from django.contrib import admin
from django.urls import path
from rainforest import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.root),
  path('products/', views.products, name="products"),
  path('products/<int:product_id>/', views.product_show, name='product_show'),
  path('products/new', views.product_new, name='product_new'),
  path('products/create', views.product_create, name='product_create'),
  path('products/<int:product_id>/edit/', views.product_edit, name='product_edit'),
  path('products/<int:product_id>/update/', views.product_update, name="product_update")
]
