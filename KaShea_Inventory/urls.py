from django.urls import path
from . import views


app_name = "KaShea_Inventory"

urlpatterns = [
    path("", views.inventory, name="inventory"),
]
