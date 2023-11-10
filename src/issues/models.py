from django.db import models
from shared.django import TimeStampMixin


class Issue(TimeStampMixin):
    title = models.CharField(max_length=30)
    body = models.CharField(max_length=30)
    junior_id = models.IntegerField()
    senior_id = models.IntegerField(null=True)
    status = models.CharField(max_length=10)

    class Meta:
        db_table = "issues"


class Massage(TimeStampMixin):
    content = models.CharField(max_length=100)
    author_id = models.IntegerField()
    issues_id = models.IntegerField()

    class Meta:
        db_table = "issues_massages"
