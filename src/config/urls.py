from django.contrib import admin
from django.urls import path
from users import api
from users.api import create_issues
from .exchange_rates import exchange_rates
from users.api import issues_all

urlpatterns = [
    path("admin/", admin.site.urls),
    path("users/all", api.user_all),
    path("users/create", api.create_user),
    path("exchange_rates/", exchange_rates),
    path("create_issues/", create_issues),
    path("issues_all/", issues_all),
]
