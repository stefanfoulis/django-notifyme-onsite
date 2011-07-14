#-*- coding: utf-8 -*-
from django import http
from notifyme_onsite.models import OnsiteNotification
from notifyme_onsite.settings import DISMISSED_NOTIFICATION_SESSION_VAR

def dismiss_notification(request, notification_id):
    user = request.user
    if user.is_anonymous():
        dismissed_notifications = request.session.get(DISMISSED_NOTIFICATION_SESSION_VAR, [])
        dismissed_notifications.append(int(notification_id))
        # remove any historical old notice id's from the past (otherwise the session will get clogged up with a lot
        # of dismissed messages over time)
        existing_notifications = [n['id'] for n in OnsiteNotification.objects.filter(user=None).values('id')]
        dismissed_notifications = [n for n in list(set(dismissed_notifications)) if n in existing_notifications]
        request.session[DISMISSED_NOTIFICATION_SESSION_VAR] = dismissed_notifications
#        request.session.modified = True
    else:
        # TODO: if OnsiteNotification is extended to handle both sticky and normal notifications, this should dismiss
        # the notice instead of deleting it.
#        notice = OnsiteNotification.objects.filter(user=user, pk=notice_id).update(dismissed=True)
        OnsiteNotification.objects.filter(user=user, pk=notification_id).delete()
    if request.is_ajax():
        return http.HttpResponse('ok')
    else:
        redirect_to = request.GET.get('next', None)
        if redirect_to:
            return http.HttpResponseRedirect(redirect_to)
        else:
            return http.HttpResponse('ok')