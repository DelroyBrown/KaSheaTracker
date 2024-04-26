from django.urls import path
from . import views


app_name = "KaShea_Documents"

urlpatterns = [
    path("", views.documents, name="documents"),
    path("upload/", views.upload_documents, name="upload_documents"),
]
