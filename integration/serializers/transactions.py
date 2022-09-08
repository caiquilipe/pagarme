from rest_framework import serializers

from integration.serializers.cards import CardsSerializer
from integration.serializers.gateway_response import GatewayResponseSerializers


class TransactionsSerializer(serializers.Serializer):
    id = serializers.CharField(required=False)
    card = CardsSerializer()
    gateway_response = GatewayResponseSerializers()
