from django.contrib.auth.models import User
from django.db import models


# Create your models here.

# paste model
# urlhash
# ContentKey - > aws
# ExpirationDate
# CreationDate


class Paste(models.Model):
    class VisibilityChoice(models.TextChoices):
        PUBLIC = 'PUBLIC'
        UNLISTED = 'UNLISTED'
        PRIVATE = 'PRIVATE'

    class FormatterChoice(models.TextChoices):
        TEXT = 'TEXT',
        C = 'C',
        C_PLUS_PLUS = 'C_PLUS_PLUS',
        SQL = 'SQL'

    paste_hash = models.CharField(max_length=10, unique=True)
    user = models.ForeignKey(User, on_delete=models.DO_NOTHING, null=True)
    title = models.CharField(max_length=50)
    content_url = models.CharField(max_length=2048)
    formatter = models.CharField(max_length=50, choices=FormatterChoice.choices)
    visibility = models.CharField(max_length=50, choices=VisibilityChoice.choices, default=VisibilityChoice.PUBLIC)
    expiration_date = models.DateTimeField()
    created_on = models.DateTimeField(auto_now_add=True)
    updated_on = models.DateTimeField(auto_now=True)
    password = models.CharField(max_length=10, null=True)
