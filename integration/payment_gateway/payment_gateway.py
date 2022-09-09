from .classes.customers import Customer
from .classes.cards import Card
from .classes.orders import Order

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
        return Customer.insert_customer(payload=payload)

    @abstractmethod
    def get_cards(customer_id):
        return Card.get_cards(customer_id=customer_id)

    @abstractmethod
    def get_card(customer_id, pk):
        return Card.get_card(customer_id=customer_id, pk=pk)

    @abstractmethod
    def insert_card(customer_id, payload):
        return Card.insert_card(customer_id=customer_id, payload=payload)

    @abstractmethod
    def get_orders():
        return Order.get_orders()

    @abstractmethod
    def get_order(pk):
        return Order.get_order(pk=pk)

    @abstractmethod
    def insert_order(payload):
        return Order.insert_order(payload=payload)
