from django.contrib import admin
from django.urls import path, include

from .admin import admin_statistics_view

urlpatterns = [
    path(
        "admin/statistics/",
        admin.site.admin_view(admin_statistics_view),
        name="admin-statistics"
    ),
    path("admin/", admin.site.urls),
    path("shop/", include("shop.urls")),
]
