import json
from django.http import JsonResponse
from .models import User
from django.db import models


def all(request):
    users = User.objects.all()
    attrs = {"id", "email", "firstname", "last_name", "password", "role"}
    results = []

    for user in users:
        payload = {attr: getattr(user, attr) for attr in attrs}
        results.append(payload)

    return JsonResponse({"result": results})


def create(request):
    if request.method != "POST":
        raise NotImplementedError('Only POST requsts')

    data = json.loads(request.body)
    user = User.objects.create(**data)

    if not user:
        raise Exception("Can not create user")

    attrs = {"id", "email", "firstname", "last_name", "password", "role"}
    payload = {attr: getattr(user, attr) for attr in attrs}

    return JsonResponse(payload)
