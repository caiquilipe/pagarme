from rest_framework import serializers

from integration.serializers.messages import MessagesSerializer


class GatewayResponseSerializers(serializers.Serializer):
    code = serializers.CharField(required=False)
    errors = MessagesSerializer(many=True)
