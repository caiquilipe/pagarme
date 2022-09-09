from rest_framework import serializers

from .cards import CardsSerializer
from .gateway_response import GatewayResponseSerializers


class TransactionsSerializer(serializers.Serializer):
    id = serializers.CharField(required=False)
    card = CardsSerializer()
    gateway_response = GatewayResponseSerializers()
