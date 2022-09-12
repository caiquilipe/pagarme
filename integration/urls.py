from integration.views.webhook import WebhookView

from django.urls import path


urlpatterns = [
    path("", WebhookView.as_view(), name="WebhookView"),
]
