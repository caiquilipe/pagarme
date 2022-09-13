from ..payment_gateway import PaymentGatewayClass
from ..models import CustomerUser

from rest_framework.exceptions import ValidationError
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.viewsets import ViewSet
from rest_framework import status




class CustomerCardsViewSet(ViewSet):
    permission_classes = [IsAuthenticated]
    @staticmethod
    def get_customer_id(user):
        customer_user = CustomerUser.objects.filter(user_ptr = user)
        if customer_user.exists():
            return customer_user.first().customer_id
        else:
            raise ValidationError(detail="Usuário não possui customer_id")

    def list(self,request):
        customer_id = self.get_customer_id(request.user)
        cards = PaymentGatewayClass.get_cards(customer_id)
        return Response(data = cards,status=status.HTTP_200_OK)

    def retrieve(self,request,pk):
        customer_id = self.get_customer_id(request.user)
        card = PaymentGatewayClass.get_card(customer_id,pk)
        return Response(data = card,status=status.HTTP_200_OK)

    def create(self,request):
        customer_id = self.get_customer_id(request.user)
        response_data = PaymentGatewayClass.insert_card(customer_id,request.data)
        return Response(data = response_data,status=status.HTTP_201_CREATED)