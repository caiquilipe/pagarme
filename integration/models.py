from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CustomerUser(User):
    identification_document = models.CharField(verbose_name="CPF", max_length=11)
    customer_id = models.CharField(max_length=255, blank=True)
    phone_number = models.CharField(max_length=255)
