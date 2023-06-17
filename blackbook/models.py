from django.db import models

class Item(models.Model):
    name = models.CharField("Name",max_length=200)
    loc = models.CharField("Item Location",max_length=200)
    dist = models.CharField("Distance",max_length=200,default="",blank=True)
    price = models.CharField("Price (GBP)",max_length=20)
    img = models.CharField("Image URL",max_length=500)

    def __str__(self): return self.name + f"({self.price})"
    
class Category(models.Model):
    name = models.CharField("Name",max_length=100)
    icon = models.CharField("Icon",max_length=100)

    def __str__(self): return self.name
