from ..serializers.customers import CustomersSerializer

from requests.auth import HTTPBasicAuth

from django.conf import settings

import requests
import json


class Customer:
    __header = {
        "Accept": "application/json",
    }
    __url = "https://api.pagar.me/core/v5/customers"

    @classmethod
    def get_customers(cls):
        content = json.loads(requests.get(cls.__url, headers=cls.__header).text)
        return CustomersSerializer(content.get("data"), many=True).data

    @classmethod
    def get_customer(cls, pk):
        cls.__url += f"/{pk}"
        content = json.loads(requests.get(cls.__url, headers=cls.__header).text)
        return CustomersSerializer(content).data

    @classmethod
    def insert_customer(cls, payload):
        cls.__header["Content-Type"] = "application/json"
        content = json.loads(
            requests.post(
                cls.__url,
                auth=HTTPBasicAuth(settings.PAGARME_SECRET_KEY, ""),
                headers=cls.__header,
                json=payload,
            ).text
        )
        return CustomersSerializer(content).data
