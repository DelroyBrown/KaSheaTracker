from django.urls import path
from . import views


app_name = "KaShea_Reports"

urlpatterns = [
    path("", views.reports, name="reports"),
]
