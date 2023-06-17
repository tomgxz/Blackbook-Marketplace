from django.urls import path

from . import views

app_name = "blackbook"

urlpatterns = [
    path("", views.index, name="index"),
]