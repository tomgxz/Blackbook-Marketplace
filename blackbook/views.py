from django.shortcuts import render,get_object_or_404,redirect
from .models import Item,Category
import json,datetime,os

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def index(request):
    return redirect("marketplace/")

def marketplace(request):
    return render(request,"index.html",{"item_list": Item.objects.order_by("id"),"category_list":Category.objects.order_by("name")})

def tracking(request):
    if is_ajax(request) and request.method == "POST":
        userdat = request.POST.get("data")
        userdat = json.loads(userdat)
        with open(f"./blackbook/data/useraccesslog/{str(datetime.datetime.now()).replace(' ','-').replace(':','-').replace('.','-')}.json","w") as f:
            f.write(json.dumps(userdat,indent=4))
    return redirect("/")