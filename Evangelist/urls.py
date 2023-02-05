from django.contrib import admin
from django.urls import path, include


urlpatterns = [
    path("admin/", admin.site.urls),
    path("accounts/", include("allauth.urls")),
    # path("", include("Payments.urls")),
    path("", include("subscriptions.urls")),
]
