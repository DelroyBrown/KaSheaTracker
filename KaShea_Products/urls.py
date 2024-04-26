from django.urls import path
from . import views


app_name = "KaShea_Products"

urlpatterns = [
    path("", views.products, name="products"),
]
