#-*- coding: utf-8 -*-
from notifyme_onsite.models import OnsiteNotice

def sticky_notices(request):
    user = request.user
    if user.is_anonymous():
        # provide an alternative for the anonymous users
        sticky_notices = []
    else:
        sticky_notices = OnsiteNotice.objects.filter(user=request.user, was_dismissed=False)
    print sticky_notices
    return {'sticky_notices': sticky_notices}
