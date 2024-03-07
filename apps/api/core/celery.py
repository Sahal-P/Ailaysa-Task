import os

from celery import Celery
from django.conf import settings

"""
Celery application configuration.

This module configures a Celery application for use with Django, allowing the use of Celery
for asynchronous task execution in the Django project.

Attributes:
    app (Celery): The Celery application instance configured for the Django project.
"""

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings")

app = Celery("core")

app.config_from_object("django.conf:settings", namespace="CELERY")

app.autodiscover_tasks()
