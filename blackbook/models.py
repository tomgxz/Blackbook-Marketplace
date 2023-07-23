from django.db import models

class Seller(models.Model):
    name = models.CharField("Name",max_length=200)
    joined = models.DateTimeField(auto_now_add=True,editable=False)
    created = models.DateTimeField(auto_now_add=True,editable=False)
    updated = models.DateTimeField(auto_now=True,editable=False)

    def __str__(self): return self.name

class Category(models.Model):
    name = models.CharField("Name",max_length=100)
    icon = models.CharField("Icon",max_length=100)

    def __str__(self): return self.name

class Item(models.Model):
    name = models.CharField("Name",max_length=200)
    desc = models.CharField("Description",max_length=1000,default="",blank=True)
    condition = models.CharField("Condition",default="",max_length=1000)
    brand = models.CharField("Brand",default="",max_length=100)
    loc = models.CharField("Item Location Name",max_length=200)
    locx = models.CharField("X Coordinate",max_length=200)
    locy = models.CharField("Y Coordinate",max_length=200)
    dist = models.CharField("Distance",max_length=200,default="",blank=True)
    price = models.FloatField("Price (GBP)")
    img = models.CharField("Image URL",max_length=500)
    created = models.DateTimeField(auto_now_add=True,editable=False)
    updated = models.DateTimeField(auto_now=True,editable=False)
    seller = models.ForeignKey(Seller,blank=True,on_delete=models.SET_NULL,null=True)
    categories = models.ManyToManyField(Category,default="",blank=True)

    def __str__(self): return self.name + f"({self.price})"

class ItemImage(models.Model):
    name = models.CharField("Referential Name",max_length=100)
    url = models.CharField("Static URL",max_length=500)
    alt = models.CharField("Alternative Text for Image",max_length=200)
    item = models.ForeignKey(Item,blank=True,on_delete=models.SET_NULL,null=True)

    def __str__(self): return self.name
    