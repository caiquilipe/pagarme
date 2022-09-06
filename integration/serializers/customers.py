from rest_framework import serializers


class CustomersSerializer(serializers.Serializer):
    id = serializers.CharField(required=False)
    name = serializers.CharField(required=True)
    email = serializers.CharField(required=False)


class CustomerInsertSerializer(serializers.Serializer):
    name = serializers.CharField(required=True)
    email = serializers.CharField(required=False)
