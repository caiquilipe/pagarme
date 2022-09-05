class Item:
    def __init__(self, name, amount, description, quantity) -> None:
        self.name = name
        self.amount = amount
        self.description = description
        self.quantity = quantity


class Customer:
    def __init__(self, name, email) -> None:
        self.name = name
        self.email = email


class Checkout:
    def __init__(
        self,
        expires_in,
        billing_address_editable,
        customer_editable,
        accepted_payment_methods,
        success_url,
    ) -> None:
        self.expires_in = expires_in
        self.billing_address_editable = billing_address_editable
        self.customer_editable = customer_editable
        self.accepted_payment_methods = accepted_payment_methods
        self.success_url = success_url


class Payments:
    def __init__(self, payment_method, checkout: Checkout) -> None:
        self.payment_method = payment_method
        self.checkout = checkout
