from django.db import models
import qrcode
from django.db.models.signals import pre_save, post_save
from django.dispatch import receiver
from CoffeeShop.settings import ALLOWED_HOSTS

# Create your models here.

class Table(models.Model):
    table_number = models.IntegerField(unique=True)
    table_QR_Code = models.ImageField(upload_to='media/table/qrCodes/',blank=True,null=True)
    busy = models.BooleanField(default=False)
    reserved= models.BooleanField(default=False)
    def __str__(self):
        return "Table "+str(self.table_number)
@receiver(pre_save, sender=Table)
def table_QR_Generation(sender, instance, *args, **kwargs):
    # Génère le code QR avec la bibliothèque qrcode
    qr = qrcode.QRCode(
        version=None,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=2,
    )
    # qr.add_data("https://"+ALLOWED_HOSTS[0]+'/'+str(instance.table_number))
    qr.add_data(instance.table_number)
    qr.make(fit=True)

    # Enregistre l'image du code QR dans un fichier
    filename = "table/qrCodes/table{}.png".format(instance.table_number)
    img = qr.make_image(fill_color="black", back_color="white")
    img.save('media/'+filename)
    instance.table_QR_Code = filename
