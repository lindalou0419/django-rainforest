from django.db import models
from django.core.validators import MinLengthValidator, MaxLengthValidator

class Product(models.Model):
  name = models.CharField(max_length=255, null=False)
  description = models.TextField(
    validators=[MinLengthValidator(10, message="The description is too short!"), MaxLengthValidator(500, message="The description is too long!")],
    null=False
  )
  price_in_cents = models.IntegerField(null=False)

  def __str__(self):
    return self.name

  def price(self):
    dollars = self.price_in_cents / 100
    return f"${dollars:.2f}"