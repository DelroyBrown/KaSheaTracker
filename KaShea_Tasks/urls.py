from django.urls import path
from . import views


app_name = "KaShea_Tasks"

urlpatterns = [
    path("", views.tasks, name="tasks"),
]
