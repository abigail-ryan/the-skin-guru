from django.db import models
from django_summernote.fields import SummernoteTextField
from django.contrib.auth.models import User
from cloudinary.models import CloudinaryField

# Create your models here.

class Category(models.Model):

    class Meta:
        verbose_name_plural = 'Categories'

    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Brand(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class SkinType(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey('Category', null=True, blank=True, on_delete=models.SET_NULL)
    brand = models.ForeignKey('Brand', null=True, blank=True, on_delete=models.SET_NULL)
    skin_type = models.ForeignKey('SkinType', null=True, blank=True, on_delete=models.SET_NULL)
    name = models.CharField(max_length=254)
    description = SummernoteTextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    product_size_ml = models.IntegerField(null=True, blank=True)
    product_size_g = models.IntegerField(null=True, blank=True)
    key_ingredients = SummernoteTextField(null=True, blank=True)
    ingredients = SummernoteTextField(null=True, blank=True)
    how_to_use = SummernoteTextField(null=True, blank=True)
    vegan = models.BooleanField(default=False)
    image = CloudinaryField('image', default='placeholder')

    def __str__(self):
        return self.name


class Review(models.Model):
    product = models.ForeignKey('products.Product', on_delete=models.CASCADE, related_name='reviews')
    user = models.ForeignKey('auth.User', on_delete=models.CASCADE, related_name='reviewer')
    rating = models.IntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # Dropdown for 1 to 5 stars
    comment = models.TextField()
    approved = models.BooleanField(default=False)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.product.name} - {self.rating} Stars'