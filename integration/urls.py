from integration.views.api_views import CustomerViewSet
from integration.views.webhook import WebhookView

from django.urls import path


urlpatterns = [
    path("customer/", CustomerViewSet.as_view({"post": "create"})),
    path("", WebhookView.as_view(), name="WebhookView"),
]
