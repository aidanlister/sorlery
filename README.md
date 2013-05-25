Sorlery -- sorl-thumbnails with django-celery
=============================================

Provides a sorl-thumbnail backend to queue thumbnail creation with Celery.
This is necessary when you have slow remote storages like Amazon S3 and you want
to avoid filesystem access in your web thread at all costs.


Installation
------------

You can install sorlery with pip, either via a tarball or git:

    pip install https://github.com/aidanlister/sorlery/zipball/master
    pip install -e git+git@github.com:aidanlister/sorlery.git#egg=sorlery-dev

Add ``sorlery`` to your ``INSTALLED_APPS`` and configure your workers as you
would normally with ``django-celery``. Swap in the new sorl backend like so:

    THUMBNAIL_BACKEND = 'sorlery.backend.QueuedThumbnailBackend'

That's it.
