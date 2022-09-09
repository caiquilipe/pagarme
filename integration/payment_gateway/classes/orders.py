from ..utils.handle_errors import handle_error_pagarme
from ..serializers.orders import OrdersSerializer

from requests.auth import HTTPBasicAuth

from django.conf import settings

import requests
import json


class Order:
    __header = {
        "Accept": "application/json",
    }
    __url = "https://api.pagar.me/core/v5/orders"

    @classmethod
    def get_orders(cls):
        content = json.loads(requests.get(cls.__url, headers=cls.__header).text)
        return OrdersSerializer(content.get("data"), many=True).data

    @classmethod
    def get_order(cls, pk):
        cls.__url += f"/{str(pk)}"
        content = json.loads(requests.get(cls.__url, headers=cls.__header).text)
        return OrdersSerializer(content).data

    @classmethod
    def insert_order(cls, payload):
        cls.__url += "/"
        cls.__header["Content-Type"] = "application/json"
        content = json.loads(
            requests.post(
                cls.__url,
                auth=HTTPBasicAuth(settings.PAGARME_SECRET_KEY, ""),
                headers=cls.__header,
                json=payload,
            ).text
        )
        serializer = OrdersSerializer(content)
        if not serializer.is_valid():
            return handle_error_pagarme(content)
        return serializer.data
