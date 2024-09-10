from django.db import models

# Create your models here.


class Client(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    company_name = models.CharField(max_length=200, null=True)
    id_number = models.IntegerField()
    mobile_number = models.CharField(max_length=15)
    email_address = models.EmailField()
    PIN_number = models.CharField(max_length=50)

    def __str__(self) -> str:
        return f"{self.first_name}"
