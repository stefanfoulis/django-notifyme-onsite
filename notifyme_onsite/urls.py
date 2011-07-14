#-*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url, include
from notifyme_onsite.views import dismiss_notification

urlpatterns = patterns('',
    url(r'^dismiss/(?P<notification_id>[\w_-]+)/$', dismiss_notification, name="notifyme_onsite_dismiss_notification"),
)
