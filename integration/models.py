from django.db import models
from django.contrib.auth.models import User

# Create your models here.


class CustomerUser(User):
    cpf = models.CharField(verbose_name="CPF", max_length=11)
    customer_id = models.CharField(max_length=255, blank=True)
    phone = models.CharField(max_length=255)
    birth_date = models.DateField(null=True)

    def get_full_name(self):
        return f"{self.first_name} {self.last_name}"

    def masked_cpf(self) -> str:
        """
        Return masked cpf

        Returns:
            str
        """
        return f"{self.cpf[:3]}.*.*-{self.cpf[9:]}"

    def masked_email(self) -> str:
        """
        Return masked email

        Returns:
            str
        """
        pieces = self.email.split("@")
        return (
            f"{pieces[0][:3]}"
            + "*" * len(pieces[0][3:])
            + "@"
            + "*" * len(pieces[1][:-3])
            + self.email[-4:]
        )
