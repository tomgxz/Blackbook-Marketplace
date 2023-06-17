from django.shortcuts import render,get_object_or_404,redirect

from .models import Item,Category

def index(request):
    return render(request,"index.html",{"item_list": Item.objects.order_by("id"),"category_list":Category.objects.order_by("name")})
