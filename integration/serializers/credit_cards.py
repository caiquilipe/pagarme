from integration.serializers.cards import CardCvvSerializer

from rest_framework import serializers


class CreditCardsSerializer(serializers.Serializer):
    capture = serializers.BooleanField(required=True)
    statement_descriptor = serializers.CharField(required=False)
    card_id = serializers.CharField(required=True)
    card = CardCvvSerializer()
