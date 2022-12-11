from django.urls import path
from django.conf import settings

from . import views 

urlpatterns = [
    path('', views.webapp, name="webapp"),
    path(settings.WEBHOOK_URL_PATH, views.handle_webhook_requests, name="webhook")
]