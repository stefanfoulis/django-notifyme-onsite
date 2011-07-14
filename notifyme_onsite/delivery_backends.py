#-*- coding: utf-8 -*-
from notifyme.delivery_backends.base import BaseDeliveryBackend
from django.template.loader import render_to_string
from notifyme_onsite.models import OnsiteNotification

class OnsiteStickyBackend(BaseDeliveryBackend):
    identifier = 'onsite_sticky'
    supports_anonymous_users = True

    def deliver_to(self, user, context, notification, language):
        expires_at = notification.options.get('expires_at', None)
        body_html = render_to_string(
            (
                "notifyme/notification_types/%s/onsite/sticky.html" % notification.identifier,
                "notifyme/notification_types/generic/onsite/sticky.html",
            ),
            context_instance=context
        )
        OnsiteNotification(
            user=user,
            language=language,
            expires_at=expires_at,
            notification_type=notification.identifier,
            sticky_body_html=body_html,
        ).save()
