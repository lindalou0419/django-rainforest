from django.contrib import admin
from django.urls import path
from rainforest import views

urlpatterns = [
  path('admin/', admin.site.urls),
  path('', views.root),
  path('products/', views.products, name="products"),
  path('products/<int:product_id>/', views.product_show, name='product_show'),
]
