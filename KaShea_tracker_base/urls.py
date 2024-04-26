from django.contrib import admin
from django.urls import path, include

app_name = "KaShea_tracker_base"

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include("KaShea_Accounts.urls")),
    path("documents/", include("KaShea_Documents.urls")),
    path("inventory/", include("KaShea_Inventory.urls")),
    path("products/", include("KaShea_Products.urls")),
    path("", include("KaShea_Reports.urls")),
    path("tasks/", include("KaShea_Tasks.urls")),
    # path("", include("KaShea_API.urls")),
]
