======================
django-notifyme-onsite
======================

This is a plugin for https://github.com/stefanfoulis/django-notifyme

``django-notifyme-onsite`` is a delivery backend for django-notifyme. It allows displaying notifications on the
website and keeps a list of per user notifications in the database. It contains hook for users to *dismiss* a
a sticky notification.

Installation
============

Dependencies:
 * django-notifyme

::

    pip install django-notifyme-onsite

Add ``notifyme_onsite`` to ``INSTALLED_APPS`` and register the backend somewhere in your project code (best in a
models.py)::

    import notifyme.delivery
    from notifyme_onsite.delivery import OnsiteStickyBackend
    notifyme.delivery.backend.register(OnsiteStickyBackend)
