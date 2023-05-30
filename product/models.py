import os

from django.db import models
from django.core.files import File
from PIL import Image
from io import BytesIO
from core.models import Business

def get_business_path_categories(instance, filename):
    return os.path.join("businesses/business_"+str(instance.id),"categories", filename)
def get_business_path_products(instance, filename):
    return os.path.join("businesses/business_"+str(instance.id),"products", filename)
class Category(models.Model):
    business = models.ForeignKey(Business, on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    icon = models.FileField(upload_to=get_business_path_categories,null=True)
    class Meta:
        ordering = ('name',)

    def __str__(self):
        return self.name
    
class Product(models.Model):
    category = models.ForeignKey(Category, related_name='products', on_delete=models.CASCADE,null=True)
    name = models.CharField(max_length=255)
    slug = models.SlugField(unique=True)
    description = models.TextField(blank=True, null=True)
    price = models.FloatField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateField(auto_now=True)
    image = models.ImageField(upload_to=get_business_path_products,default='default/default.png', blank=True, null=True)
    # thumbnail = models.ImageField(upload_to='upload', blank=True, null=True)

    class Meta:
        ordering = ('created_at', )

    def __str__(self):
        return self.name
    
    # def get_display_price(self):
    #     return self.price / 1000

    # def get_thumbnail(self):
    #     if self.thumbnail:
    #         return self.thumbnail.url
    #     else:
    #         if self.image:
    #             self.thumbnail = self.make_thumbnail(self.image)
    #             self.save()
    #
    #             return self.thumbnail.url
    #         else:
    #             return 'https://via.placeholder.com/240x240.jpg'

    # def make_thumbnail(self, image, size=(300, 300)):
    #     img = Image.open(image)
    #     img.convert('RGB')
    #     img.thumbnail(size)
    #
    #     thumb_io = BytesIO()
    #     img.save(thumb_io, 'JPEG', quality=85)
    #
    #     thumbnail = File(thumb_io, name=image.name)
    #
    #     return thumbnail