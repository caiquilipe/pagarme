from integration.views.customer_viewset import CustomerViewSet
from integration.views.webhook import WebhookView

from django.urls import path


urlpatterns = [
    path("customer/", CustomerViewSet.as_view({"post": "create"})),
    path("", WebhookView.as_view(), name="WebhookView"),
]
