from ..utils.handle_errors import handle_error_pagarme
from ..serializers.cards import CardsSerializer

from requests.auth import HTTPBasicAuth

from django.conf import settings

import requests
import json


class Card:
    __header = {
        "Accept": "application/json",
    }
    __url = "https://api.pagar.me/core/v5/customers/ /cards"

    @classmethod
    def get_cards(cls, customer_id):
        cls.__url = cls.__url.replace(" ", str(customer_id))
        content = json.loads(
            requests.get(
                cls.__url,
                auth=HTTPBasicAuth(settings.PAGARME_SECRET_KEY, ""),
                headers=cls.__header,
            ).text
        )
        serializer = CardsSerializer(data=content.get("data"), many=True)
        if not serializer.is_valid():
            return handle_error_pagarme(content)
        return serializer.data

    @classmethod
    def get_card(cls, customer_id, pk):
        cls.__url = cls.__url.replace(" ", str(customer_id))
        cls.__url += f"/{str(pk)}"
        content = json.loads(
            requests.get(
                cls.__url,
                auth=HTTPBasicAuth(settings.PAGARME_SECRET_KEY, ""),
                headers=cls.__header,
            ).text
        )
        serializer = CardsSerializer(data=content)
        if not serializer.is_valid():
            return handle_error_pagarme(content)
        return serializer.data

    @classmethod
    def insert_card(cls, customer_id, payload):
        cls.__url = cls.__url.replace(" ", str(customer_id))
        cls.__header["Content-Type"] = "application/json"
        content = json.loads(
            requests.post(
                cls.__url,
                auth=HTTPBasicAuth(settings.PAGARME_SECRET_KEY, ""),
                headers=cls.__header,
                json=payload,
            ).text
        )
        serializer = CardsSerializer(data=content)
        if not serializer.is_valid():
            return handle_error_pagarme(content)
        return serializer.data
