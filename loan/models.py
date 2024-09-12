from datetime import date
from django.db import models
from django.utils import timezone


# class LOAN_STATUS_CHOICES(models.TextChoices):
#     ACTIVE = 'ACTIVE', 'ACTIVE'
#     COMPLETE = 'COMPLETE', 'COMPLETE'


class Loan(models.Model):
    loan_batch_number = models.IntegerField(default=1)
    bank = models.ForeignKey('Bank', on_delete=models.CASCADE, default=1)
    deposit_amount = models.DecimalField(decimal_places=2, max_digits=20)
    loan_amount = models.DecimalField(max_digits=20, decimal_places=2)
    loan_status = models.CharField(
        max_length=200)
    loan_start_date = models.DateField(default=date.today)
    loan_end_date = models.DateField(default=date.today)
    loan_period = models.FloatField(default=0.0)

    def __str__(self):
        return str(self.loan_batch_number)

    # @property
    # def loan_period(self):
    #     return (self.loan_end_date - self.loan_start_date).days


class Bank(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self) -> str:
        return self.name


class LoanRequirement(models.Model):
    loan = models.ForeignKey(
        Loan, on_delete=models.CASCADE, related_name='loan_requirements')
    id_file = models.FileField(upload_to='client/ID')
    pin_file = models.FileField(upload_to='client/PIN')
    offer_letter = models.FileField(upload_to='client/offer-letters')
    tracking_certificate = models.FileField(upload_to='tracking/certificate')
    tracking_invoice = models.FileField(upload_to='tracking/invoice')
    tracking_vendor = models.FileField(upload_to='tracking/vendors')
    insurance_certificate = models.FileField(
        upload_to='other/insurance-certificates')
