from rest_framework import serializers

from integration.serializers.customers import CustomersSerializer
from integration.serializers.items import ItemsSerializer
from integration.serializers.transactions import TransactionsSerializer


class ChargesSerializer(serializers.Serializer):
    id = serializers.CharField(required=False)
    gateway_id = serializers.CharField(required=False)
    amount = serializers.IntegerField(required=False)
    paid_amount = serializers.IntegerField(required=False)
    status = serializers.CharField(required=False)
    currency = serializers.CharField(required=False)
    payment_method = serializers.CharField(required=False)
    customer = CustomersSerializer()
    last_transaction = TransactionsSerializer()
