#-*- coding: utf-8 -*-
from datetime import datetime
from django.db.models.query_utils import Q
from django.utils.translation import get_language
from notifyme_onsite.models import OnsiteNotification
from notifyme_onsite.settings import DISMISSED_NOTIFICATION_SESSION_VAR

def sticky_notifications(request):
    user = request.user
    notifications = OnsiteNotification.objects.filter(
        Q(expires_at__isnull=True) | Q(expires_at__gte=datetime.now())
    )
    # TODO: Cache
    if user.is_anonymous():
        # provide an alternative for the anonymous users
        language = get_language()
        notifications = notifications.filter(user=None, language=language)
        # remove any notices that have been dismissed by the anonymous user in his session
        dismissed = request.session.get(DISMISSED_NOTIFICATION_SESSION_VAR, [])
        notifications = [n for n in notifications if not n.id in dismissed]
    else:
        notifications = notifications.filter(user=request.user)
    return {'sticky_notifications': notifications}
