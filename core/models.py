import os
from django.db import models
from django.contrib.auth.models import AbstractUser


ACCOUNT_TYPES=(
    (0,'Gérant'),
    (1,'Opérateur'),
)

BUSINESS_TYPES=(
    (0,"Non Défini"),
    (1,"Restaurant"),
    (2,"Hotel"),
    (3,"Café"),
    (4,"Café-Resto"),
    (5,"Bar"),
    (6,"Traiteur"),
)
COUNTRIES = (
    ('DZ', 'Algérie'),
    ('BE', 'Belgique'),
    ('CA', 'Canada'),
    ('FR', 'France'),
    ('HU', 'Hongrie'),
    ('IT', 'Italie'),
    ('LB', 'Liban'),
    ('TN', 'Tunisie'),
    ('UK', 'Royaume-Uni'),
    ('USA', 'États-Unis'),
)


# Create your models here.
def get_business_path_logo(instance, filename):
    return os.path.join("businesses/business_"+str(instance.id),"logo", filename)
class Business(models.Model):
    type = models.IntegerField(choices=BUSINESS_TYPES,default=0)
    name = models.CharField(max_length=60)
    description = models.TextField()
    country = models.CharField(max_length=30, choices=COUNTRIES)
    phone = models.CharField(max_length=20)
    address = models.TextField()
    logo = models.ImageField(upload_to=get_business_path_logo)
    # pays
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.name
    class Meta:
        verbose_name_plural = "Businesses"


class Account(AbstractUser):
    type = models.IntegerField(choices=ACCOUNT_TYPES, default=1)
    business = models.ForeignKey(Business,on_delete=models.CASCADE,null=True)
    phone = models.CharField(max_length=20)



