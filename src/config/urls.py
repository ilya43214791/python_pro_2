from django.contrib import admin
from django.urls import path
from users import api
from .exchange_rates import exchange_rates

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/all", api.all),
    path("users/create", api.create),
    path("exchange_rates/", exchange_rates),
]
