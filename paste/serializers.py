import datetime

from django.utils import timezone
from rest_framework import serializers

from paste.models import Paste


class PasteSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=50)
    textData = serializers.CharField(max_length=5000)
    formatter = serializers.ChoiceField(choices=Paste.FormatterChoice.choices, default=Paste.FormatterChoice.TEXT)
    visibility = serializers.ChoiceField(choices=Paste.VisibilityChoice.choices, default=Paste.VisibilityChoice.PUBLIC)
    expirationDate = serializers.DateTimeField(default=(timezone.now() + datetime.timedelta(days=10)))
    password = serializers.CharField(max_length=10, required=False, default=None)
