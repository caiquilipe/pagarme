from integration.serializers.customers import CustomerInsertSerializer
from integration.services.customers import PaymentGatewayClass

from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status


class CustomersView(APIView):
    def post(self, request):
        try:
            serializer = CustomerInsertSerializer(data=request.data)
            if not serializer.is_valid():
                raise ValidationError(serializer.errors)
            return Response(
                data=PaymentGatewayClass.insert_customers(payload=serializer.data),
                status=status.HTTP_201_CREATED,
            )
        except ValidationError as ve:
            raise ve

    def get(self, request):
        return Response(
            data=PaymentGatewayClass.get_customers(),
            status=status.HTTP_200_OK,
        )
