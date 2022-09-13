from ..utils.handle_errors import handle_error_serializer
from ..payment_gateway import PaymentGatewayClass
from ..serializers.customers import (
    CustomerInsertModelSerializer,
    UserGetOrCreateSerializer,
)
from ..models import CustomerUser

from rest_framework.exceptions import ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status


from django.db import transaction


class CustomerViewSet(ViewSet):
    permission_classes = [AllowAny]

    @staticmethod
    def send_user_and_save_customer_id(user: CustomerUser):
        payload = CustomerInsertModelSerializer(user).data
        customer_id = PaymentGatewayClass.insert_customer(payload).get("id")
        user.customer_id = customer_id
        user.save()

    def create(self, request):
        with transaction.atomic():
            serializer = UserGetOrCreateSerializer(data=request.data)
            if not serializer.is_valid():
                raise ValidationError(detail=handle_error_serializer(serializer.errors))
            user = serializer.save()
            self.send_user_and_save_customer_id(user)
            return Response(
                data=UserGetOrCreateSerializer(user).data,
                status=status.HTTP_201_CREATED,
            )


