from cProfile import label
from unicodedata import name
from django.forms import ModelForm
from django import forms

from integration.models import CustomerUser


class CustomerCreateForm(forms.Form):
    first_name = forms.CharField(label="Primeiro Nome")
    last_name = forms.CharField(label="Ultimo Nome")
    email = forms.EmailField()
    identification_document = forms.CharField(label="CPF")
    phone_number = forms.CharField(label="Número de telefone")
    senha = forms.CharField(widget=forms.PasswordInput())


class CustomerLoginForm(forms.Form):
    identification_document = forms.CharField(label="CPF")
    senha = forms.CharField(widget=forms.PasswordInput())
