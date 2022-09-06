from integration.views.customers import CustomersView
from integration.views.webhook import WebhookView

from django.urls import path


urlpatterns = [
    path("customers", CustomersView.as_view(), name="CustomersView"),
    path("", WebhookView.as_view(), name="WebhookView"),
]
