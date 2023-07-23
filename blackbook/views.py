from django.shortcuts import render,get_object_or_404,redirect
from django.http import Http404
from geopy.geocoders import Nominatim
from geopy.exc import GeocoderUnavailable
from .models import Item,Category,ItemImage
import json,datetime,re,geocoder,humanize,locale

def is_ajax(request):
    return request.META.get('HTTP_X_REQUESTED_WITH') == 'XMLHttpRequest'

def index(request):
    return redirect("marketplace/")

def marketplace(request):
    locale.setlocale(locale.LC_ALL,"")

    item_list = Item.objects.order_by("id");output = []
    for item in item_list: output.append([item,re.sub('[^0-9a-zA-Z]+', '_', item.name)])

    output = []

    for item in item_list:

        try: 
            itemLoc = Nominatim(user_agent="GetLoc").reverse(f"{item.locx}, {item.locy}")
            itemLoc = itemLoc.raw["address"]
            itemLoc = f"{itemLoc.get('town','')}, {itemLoc.get('country','')}"
        except GeocoderUnavailable as e: itemLoc = "Unknown"
        except AttributeError as e: itemLoc = "Unknown"

        mainImageExists = True
        try: 
            mainImage = ItemImage.objects.filter(item=item)[0]
            mainImageURL = mainImage.url.split(".")
            mainImageURL.insert(-1,"square")
            mainImageURL = ".".join(mainImageURL)
        except Exception as e: mainImageExists = False

        output.append({
            "id": item.id,
            "name": item.name,
            "reducedName": re.sub('[^0-9a-zA-Z]+', '_', item.name),
            "locName": itemLoc,
            "locXCoord": item.locx,
            "locYCoord": item.locy,
            "distance": item.dist,
            "created": item.created,
            "updated": item.updated,
            "createdDist": humanize.naturaldelta(datetime.datetime.now() - item.created.replace(tzinfo=None)),
            "price": locale.currency(item.price,grouping=True),
            "imageURL": item.img,
            "images": [*ItemImage.objects.filter(item=item)],
            "mainImage": {
                "name":mainImage.name if mainImageExists else "",
                "url":mainImageURL if mainImageExists else "",
                "alt":mainImage.alt if mainImageExists else "",
                "item":mainImage.item if mainImageExists else None,
            },
            "seller": {
                "id": item.seller.id,
                "name": item.seller.name,
                "reducedName": re.sub('[^0-9a-zA-Z]+', '_', item.seller.name),
                "created": item.seller.created,
                "updated": item.seller.updated,
                "createdYear": item.seller.created.year,
            },
        })

    return render(request,"index.html",{"item_list": output,"category_list":Category.objects.order_by("name")})

def marketplaceItem(request,item_id,item_name):
    locale.setlocale(locale.LC_ALL,"")

    item = get_object_or_404(Item, pk=item_id)

    try: 
        itemLoc = Nominatim(user_agent="GetLoc").reverse(f"{item.locx}, {item.locy}")
        itemLoc = itemLoc.raw["address"]
        itemLoc = f"{itemLoc.get('town','')}, {itemLoc.get('country','')}"
    except GeocoderUnavailable as e: itemLoc = "Unknown"
    except AttributeError as e: itemLoc = "Unknown"

    mainImageExists = True
    try: 
        mainImage = ItemImage.objects.filter(item=item)[0]
        mainImageURL = mainImage.url.split(".")
        mainImageURL.insert(-1,"square")
        mainImageURL = ".".join(mainImageURL)
    except Exception as e: mainImageExists = False

    newitem = {
        "id": item.id,
        "name": item.name,
        "reducedName": re.sub('[^0-9a-zA-Z]+', '_', item.name),
        "desc":item.desc,
        "condition":item.condition,
        "brand":item.brand,
        "locName": itemLoc,
        "locXCoord": item.locx,
        "locYCoord": item.locy,
        "distance": item.dist,
        "created": item.created,
        "updated": item.updated,
        "createdDist": humanize.naturaldelta(datetime.datetime.now() - item.created.replace(tzinfo=None)),
        "price": locale.currency(item.price,grouping=True),
        "imageURL": item.img,
        "images": [*ItemImage.objects.filter(item=item)],
        "mainImage": {
            "name":mainImage.name if mainImageExists else "",
            "url":mainImageURL if mainImageExists else "",
            "alt":mainImage.alt if mainImageExists else "",
            "item":mainImage.item if mainImageExists else None,
        },
        "seller": {
            "id": item.seller.id,
            "name": item.seller.name,
            "reducedName": re.sub('[^0-9a-zA-Z]+', '_', item.seller.name),
            "created": item.seller.created,
            "updated": item.seller.updated,
            "createdYear": item.seller.created.year,
        },
    }

    g = geocoder.ip('me')

    try:
        userdat = {
            "currentX":g.latlng[0],
            "currentY":g.latlng[1]
        }
    except TypeError as e:
        userdat = {}

    if item_name == re.sub('[^0-9a-zA-Z]+', '_', item.name): 
        return render(request, "item.html", {"item": newitem,"userdat":userdat}) 
    else: raise Http404


def tracking(request):
    if is_ajax(request) and request.method == "POST":
        userdat = request.POST.get("data")
        userdat = json.loads(userdat)
        with open(f"./blackbook/data/useraccesslog/{str(datetime.datetime.now()).replace(' ','-').replace(':','-').replace('.','-')}.json","w") as f:
            f.write(json.dumps(userdat,indent=4))
    return redirect("/")