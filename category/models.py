from django.db import models
from django.urls import reverse


# Create your models here.
class Category(models.Model):
    name = models.CharField(max_length=50, unique=True)
    slug = models.SlugField(max_length=50, unique=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to="photoes\categories", blank=True)


    def __str__(self):
        return self.name


    def get_url(self):
        return reverse('product_by_category', args=[self.slug])
