from .serializers.customers import CustomerInsertSerializer
from .utils.handle_errors import handle_error_serializer
from .serializers.orders import OrdersInserirSerializer
from .serializers.cards import CardsInsertSerializer
from .classes.customers import Customer
from .classes.orders import Order
from .classes.cards import Card

from rest_framework.exceptions import ValidationError

from abc import abstractmethod


class PaymentGatewayClass:
    @abstractmethod
    def get_customers():
        return Customer.get_customers()

    @abstractmethod
    def get_customer(pk):
        return Customer.get_customer(pk=pk)

    @abstractmethod
    def insert_customer(payload):
        try:
            serializer = CustomerInsertSerializer(data=payload)
            if not serializer.is_valid():
                raise ValidationError(detail=handle_error_serializer(serializer.errors))
            return Customer.insert_customer(payload=serializer.data)
        except ValidationError as ve:
            raise ve

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
                raise ValidationError(detail=handle_error_serializer(serializer.errors))
            return Card.insert_card(customer_id=customer_id, payload=serializer.data)
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
        try:
            serializer = OrdersInserirSerializer(data=payload)
            if not serializer.is_valid():
                raise ValidationError(detail=handle_error_serializer(serializer.errors))
            return Order.insert_order(payload=serializer.data)
        except ValidationError as ve:
            raise ve
