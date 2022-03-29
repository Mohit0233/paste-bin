import _hashlib
import datetime
import hashlib
import time

from django.utils import timezone

from paste.models import Paste
from paste.services import firebase_storage


def add_paste(title, text_data, user_id, formatter=Paste.FormatterChoice.TEXT, visibility=Paste.VisibilityChoice.PUBLIC,
              expiration_date=timezone.now() + datetime.timedelta(days=10), password=None):
    paste_hash = hashlib.md5((title + text_data + (user_id if user_id else "") + time.time().__str__()).encode()).hexdigest()[:7]

    content_url = firebase_storage.update_media_and_get_url(text_data, content_type='text/plain')

    paste_object = Paste(paste_hash=paste_hash, title=title, user_id=user_id, content_url=content_url,
                         formatter=formatter, visibility=visibility, expiration_date=expiration_date, password=password)
    paste_object.save()
    return paste_object
