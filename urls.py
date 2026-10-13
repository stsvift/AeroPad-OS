from django.contrib import admin
from django.urls import path
from core.views import enter, home

urlpatterns = [
    path("", enter),
    path("home/", home),
    path("admin/", admin.site.urls),
]

