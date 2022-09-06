from abc import abstractmethod
from integration.classes.customers import Customer


class PaymentGatewayClass:
    @abstractmethod
    def get_customers():
        return Customer.get_customers()

    @abstractmethod
    def insert_customers(payload):
        return Customer.insert_customers(payload)
