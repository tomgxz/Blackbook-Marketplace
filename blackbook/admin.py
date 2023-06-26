from django.contrib import admin

from .models import Item,Category,Seller,ItemImage

admin.site.register(Item)
admin.site.register(ItemImage)
admin.site.register(Category)
admin.site.register(Seller)