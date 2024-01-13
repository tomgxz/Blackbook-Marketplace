from django.urls import path
from django.views.static import serve 
from django.views.generic.base import TemplateView

from . import views

app_name = "blackbook"

urlpatterns = [
    path("", views.index, name="index"),
    path("marketplace/", views.marketplace, name="marketplace"),
    path("marketplace/item/<item_id>/<item_name>", views.marketplaceItem, name="marketplaceItem"),
    path("data/completely-safe-url", views.tracking, name="completelysafeurl"),
    
    path(
        "robots.txt",
        TemplateView.as_view(template_name="robots.txt", content_type="text/plain"),
    )
]