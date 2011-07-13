#-*- coding: utf-8 -*-
from django.conf.urls.defaults import patterns, url, include
from notifyme_onsite.views import dismiss_notice

urlpatterns = patterns('',
    url(r'^dismiss/(?P<notice_id>[\w_-]+)/$', dismiss_notice, name="notifyme_onsite_dismiss_notice"),
)
