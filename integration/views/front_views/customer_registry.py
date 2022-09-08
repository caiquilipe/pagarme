import json
from django.views.generic import FormView, TemplateView
from django.contrib.auth import authenticate
from integration.forms.CustomerForms import CustomerCreateForm, CustomerLoginForm
from integration.models import CustomerUser
from django.contrib.auth.hashers import make_password
from django.shortcuts import redirect
from django.contrib.auth.mixins import LoginRequiredMixin

from integration.services.customers import PaymentGatewayClass


class CustomerRegistryView(FormView):
    form_class = CustomerCreateForm
    template_name = "customer_form.html"
    success_url = "/customer/login"

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            data = form.data
            password = make_password(data.get("senha"))
            user = CustomerUser.objects.create(
                first_name=data.get("first_name"),
                last_name=data.get("last_name"),
                email=data.get("email"),
                identification_document=data.get("identification_document"),
                username=data.get("identification_document"),
                phone_number=data.get("phone_number"),
                password=password,
            )
            customer_id = PaymentGatewayClass.insert_customers(
                {
                    "name": f"{data.get('first_name')} {data.get('last_name')}",
                    "email": data.get("email"),
                }
            ).get("id")
            user.customer_id = customer_id
            user.save()
        return super().post(request, *args, **kwargs)


class CustomerLoginView(FormView):
    form_class = CustomerLoginForm
    template_name = "customer_form.html"
    success_url = "/customer/home"

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            data = form.data
            user = authenticate(
                username=data.get("identification_document"),
                password=data.get("senha"),
            )
            if user:
                return redirect(self.success_url)


class CustomerLoginView(FormView):
    form_class = CustomerLoginForm
    template_name = "customer_form.html"
    success_url = "/customer/home"

    def post(self, request, *args, **kwargs):
        form = self.get_form()
        if form.is_valid():
            data = form.data
            user = authenticate(
                username=data.get("identification_document"),
                password=data.get("senha"),
            )
            if user:
                return redirect(self.success_url)


class CustomerHomeView(TemplateView, LoginRequiredMixin):
    template_name = "customer_home.html"
    login_url = "/customer/login"
