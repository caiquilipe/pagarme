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
        cls.__url.replace(" ", customer_id)
        print(cls.__url)
        content = json.loads(requests.get(cls.__url, headers=cls.__header).text)
        return CardsSerializer(content.get("data"), many=True).data

    @classmethod
    def get_card(cls, customer_id, pk):
        cls.__url.replace(" ", customer_id)
        cls.__url += f"/{pk}"
        content = json.loads(requests.get(cls.__url, headers=cls.__header).text)
        return CardsSerializer(content).data

    @classmethod
    def insert_card(cls, customer_id, payload):
        cls.__ur = cls.__url.replace(" ", customer_id)
        cls.__header["Content-Type"] = "application/json"
        content = json.loads(
            requests.post(
                cls.__url,
                auth=HTTPBasicAuth(settings.PAGARME_SECRET_KEY, ""),
                headers=cls.__header,
                json=payload,
            ).text
        )
        return CardsSerializer(content).data
