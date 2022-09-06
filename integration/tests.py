from django.test.testcases import TransactionTestCase
from django.urls import reverse

from rest_framework.test import APIClient
from rest_framework import status


class CustomersTestCase(TransactionTestCase):
    reset_sequences = True

    def setUp(self) -> None:
        self.client = APIClient()
        return super().setUp()

    def test_get_customers(self):
        response = self.client.get(reverse("CustomersView"))
        self.assertEquals(response.status_code, status.HTTP_200_OK)

    def test_insert_customers(self):
        payload = {"name": "test", "email": "test@test.com"}
        response = self.client.post(reverse("CustomersView"), payload)
        print(response.data)
        self.assertEquals(response.status_code, status.HTTP_201_CREATED)
