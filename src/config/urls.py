from django.contrib import admin
from django.urls import path
from users import api

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/all", api.all),
    path("users/create", api.create),
    path("currency_exchange", api.create),
]
