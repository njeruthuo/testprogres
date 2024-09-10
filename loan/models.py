from datetime import date
from django.db import models
from django.utils import timezone


class LOAN_STATUS_CHOICES(models.TextChoices):
    ACTIVE = 'ACTIVE', 'ACTIVE'
    COMPLETE = 'COMPLETE', 'COMPLETE'


class Loan(models.Model):
    loan_id = models.IntegerField()
    deposit_amount = models.DecimalField(decimal_places=2, max_digits=20)
    loan_amount = models.DecimalField(max_digits=20, decimal_places=2)
    loan_status = models.CharField(
        max_length=200, choices=LOAN_STATUS_CHOICES.choices)
    loan_start_date = models.DateField(default=timezone.now)
    loan_end_date = models.DateField()
    loan_period = models.FloatField()

    def __str__(self):
        return str(self.loan_id)

    # @property
    # def loan_period(self):
    #     return (self.loan_end_date - self.loan_start_date).days


class Bank(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class LoanRequirement(models.Model):
    loan = models.ForeignKey(Loan, on_delete=models.CASCADE, default=None)
    id_file = models.FileField(upload_to='client/ID')
    pin_file = models.FileField(upload_to='client/PIN')
    offer_letter = models.FileField(upload_to='client/offer-letters')
    tracking_certificate = models.FileField(upload_to='tracking/certificate')
    tracking_invoice = models.FileField(upload_to='tracking/invoice')
    tracking_vendor = models.FileField(upload_to='tracking/vendors')
    insurance_certificate = models.FileField(
        upload_to='other/insurance-certificates')
