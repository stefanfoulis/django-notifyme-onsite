#-*- coding: utf-8 -*-
from django.contrib import admin

from notifyme_onsite.models import OnsiteNotice

class OnsiteNoticeAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'user', 'notice_type', 'language', 'sticky_body_html', 'expires_at',)

admin.site.register(OnsiteNotice, OnsiteNoticeAdmin)