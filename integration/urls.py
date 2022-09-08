from integration.views.front_views.customer_registry import (
    CustomerHomeView,
    CustomerLoginView,
    CustomerRegistryView,
)
from integration.views.webhook import WebhookView

from django.urls import path


urlpatterns = [
    path("customer/login", CustomerLoginView.as_view()),
    path("customer/home", CustomerHomeView.as_view()),
    path("customer/request", CustomerHomeView.as_view()),
    path("customer/registry", CustomerRegistryView.as_view()),
    path("", WebhookView.as_view(), name="WebhookView"),
]
