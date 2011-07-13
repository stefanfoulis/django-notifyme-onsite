#-*- coding: utf-8 -*-
from django import http
from notifyme_onsite.models import OnsiteNotice

def dismiss_notice(request, notice_id):
    user = request.user
    if user.is_anonymous():
        dismissed_notices = request.session.get('dismissed_notices', [])
        dismissed_notices.append(int(notice_id))
        # remove any historical old notice id's from the past (otherwise the session will get clogged up with a lot
        # of dismissed messages over time)
        existing_notices = [n['id'] for n in OnsiteNotice.objects.filter(user=None).values('id')]
        dismissed_notices = [n for n in dismissed_notices if n in existing_notices]
        request.session['dismissed_notices'] = dismissed_notices
    else:
        # TODO: if OnsiteNotice is extended to handle both sticky and normal notifications, this should dismiss
        # the notice instead of deleting it.
#        notice = OnsiteNotice.objects.filter(user=user, pk=notice_id).update(dismissed=True)
        OnsiteNotice.objects.filter(user=user, pk=notice_id).delete()
    if request.is_ajax():
        return http.HttpResponse('ok')
    else:
        redirect_to = request.GET.get('next', None)
        if redirect_to:
            return http.HttpResponseRedirect(redirect_to)
        else:
            return http.HttpResponse('ok')