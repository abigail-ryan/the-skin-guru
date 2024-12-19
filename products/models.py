from django.db import models
from django_summernote.fields import SummernoteTextField

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
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

    def __str__(self):
        return self.name