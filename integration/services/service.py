from integration.classes.customers import Customer
from integration.classes.card import Card

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
    def get_cards():
        return Card.get_cards()

    @abstractmethod
    def get_card(customer_id, pk):
        return Card.get_card(customer_id=customer_id, pk=pk)

    @abstractmethod
    def insert_card(customer_id, payload):
        return Card.insert_card(customer_id=customer_id, payload=payload)
