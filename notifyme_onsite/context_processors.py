#-*- coding: utf-8 -*-
from datetime import datetime
from django.db.models.query_utils import Q
from django.conf import settings
from notifyme_onsite.models import OnsiteNotice

def sticky_notices(request):
    user = request.user
    notices = OnsiteNotice.objects.filter(
        Q(expires_at__isnull=True) | Q(expires_at__gte=datetime.now())
    )
    if user.is_anonymous():
        # provide an alternative for the anonymous users
        language = request.session.get('django_language', settings.LANGUAGE_CODE)
        notices = notices.filter(user=None, language=language)
        # remove any notices that have been dismissed by the anonymous user in his session
        dismissed = request.session.get('dismissed_notices', [])
        notices = [n for n in notices if not n.id in dismissed]
    else:
        notices = OnsiteNotice.objects.filter(user=request.user)
    return {'sticky_notices': notices}
