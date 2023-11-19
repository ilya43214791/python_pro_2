import json
from django.http import JsonResponse
from .models import User, Issues
from django.db import models


def user_all(request):
    users = User.objects.all()
    attrs = {"id", "email", "first_name", "last_name", "password", "role"}
    results = []

    for user in users:
        payload = {attr: getattr(user, attr) for attr in attrs}
        results.append(payload)

    return JsonResponse({"result": results})


def create_user(request):
    if request.method != "POST":
        raise NotImplementedError('Only POST requsts')

    data = json.loads(request.body)
    user = User.objects.create(**data)

    if not user:
        raise Exception("Can not create user")

    attrs = {"id", "email", "first_name", "last_name", "password", "role"}
    payload = {attr: getattr(user, attr) for attr in attrs}

    return JsonResponse(payload)


def create_issues(request):
    if request.method != "POST":
        raise NotImplementedError('Only POST requsts')

    data = json.loads(request.body)
    issues = Issues.objects.create(**data)

    if not issues:
        raise Exception("Can not create user")

    attrs = {"title", "body", "junior_id", "senior_id", "status", }
    payload = {attr: getattr(issues, attr) for attr in attrs}

    return JsonResponse(payload)


def issues_all(request):
    issues = Issues.objects.all()
    attrs = {"title", "body", "junior_id", "senior_id", "status",}
    results = []

    for issuess in issues:
        payload = {attr: getattr(issuess, attr) for attr in attrs}
        results.append(payload)

    return JsonResponse({"result": results})
