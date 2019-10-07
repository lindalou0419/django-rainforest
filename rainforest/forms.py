from django.forms import ModelForm
# from django import forms
from rainforest.models import Product, Review

class ProductForm(ModelForm):
  class Meta:
    model = Product
    fields = ['name', 'description', 'price_in_cents']
#-------------------------------

class ReviewForm(ModelForm):
  class Meta:
    model = Review
    fields = ['comment']

  def clean(self):
    data = super().clean()
    content = data.get("comment")
    if len(content) < 3 or len(content) > 1000:
      self.add_error("comment", "Reviews must be between 10 to 1000 characters.")