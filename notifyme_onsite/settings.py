#-*- coding: utf-8 -*-
from django.conf import settings

DISMISSED_NOTIFICATION_SESSION_VAR = getattr(settings, 'NOTIFYME_ONSITE_DISMISSED_NOTIFICATION_SESSION_VAR', 'NOTIFYME_ONSITE_DISMISSED_NOTIFICATIONS')
