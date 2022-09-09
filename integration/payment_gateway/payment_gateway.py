from integration.payment_gateway.serializers.cards import CardsInsertSerializer
from .classes.customers import Customer
from .classes.cards import Card
from .classes.orders import Order
from rest_framework.exceptions import ValidationError


from abc import abstractmethod


class PaymentGatewayClass:
    @abstractmethod
    def get_customers():
        try:
            data = Customer.get_customers()
            return data
        except:
            return "erro"

    @abstractmethod
    def get_customer(pk):

        return Customer.get_customer(pk=pk)

    @abstractmethod
    def insert_customer(payload):
        return Customer.insert_customer(payload=payload)

    @abstractmethod
    def get_cards(customer_id):
        return Card.get_cards(customer_id=customer_id)

    @abstractmethod
    def get_card(customer_id, pk):
        return Card.get_card(customer_id=customer_id, pk=pk)

    @abstractmethod
    def insert_card(customer_id, payload):
        try:
            serializer = CardsInsertSerializer(data=payload)
            if not serializer.is_valid():
                raise ValidationError(detail=serializer.errors)
            return Card.insert_card(customer_id=customer_id, payload=payload)
        except ValidationError as ve:
            raise ve

    @abstractmethod
    def get_orders():
        return Order.get_orders()

    @abstractmethod
    def get_order(pk):
        return Order.get_order(pk=pk)

    @abstractmethod
    def insert_order(payload):
        return Order.insert_order(payload=payload)
