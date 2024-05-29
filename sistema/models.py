from unicodedata import category
from django.db import models

# Create your models here.
class  Producto(models.Model):
    
    nombre = models.CharField(max_length=50)
    precio = models.IntegerField()
    stock= models.CharField(max_length=100)
    #categoria =models.CharField(null=False)

    def str (self):
        return str(self.nombre)+ " " +str(self.precio) + " "  + str(self.stock)
    