#-*- coding: utf-8 -*-
from django.db import models
from django.contrib.auth.models import User
import notifyme.notice

class OnsiteNotice(models.Model):
    """
    Represents a sticky notice for a user. E.g a "growl-style" notice that stays (over multiple requests) visible until
    it is dismissed by the user or it expires.

    This Model could be extended to also be used for regular notifications by adding
    a is_sticky boolean and a seperate body_html for displaying in a timeline.
    """
    created_at = models.DateTimeField(auto_now_add=True)
    notice_type = models.CharField(max_length=255, choices=notifyme.notice.types.items())
    user = models.ForeignKey(User)
    expires_at = models.DateTimeField(null=True, blank=True)
    was_dismissed = models.BooleanField(default=False)
    sticky_body_html = models.TextField(default='')