from django.urls import path
from . import views


app_name = 'KaShea_Accounts'

urlpatterns = [
    path("", views.login_view, name="login"),
]
