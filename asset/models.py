import requests
from django.db import models
from loan.models import Loan
from clients.models import Client
from remedial.models import Remedial

# Status fetch automation tool
from .util import get_post_data


class Asset(models.Model):
    vehicle_reg_no = models.CharField(max_length=100)
    make_and_model = models.CharField(max_length=200)
    asset_value = models.DecimalField(decimal_places=2, max_digits=20)
    purchase_price = models.DecimalField(decimal_places=2, max_digits=20)
    chasis = models.CharField(max_length=200)
    dealer = models.CharField(max_length=200)
    tracking_status = models.CharField(max_length=200)
    asset_type = models.CharField(max_length=25)
    color = models.CharField(max_length=100)
    insurance_value = models.DecimalField(decimal_places=2, max_digits=20)
    engine = models.CharField(max_length=100)
    asset_status = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.vehicle_reg_no

    class Meta:
        indexes = [
            models.Index(fields=['asset_status']),
            models.Index(fields=['vehicle_reg_no']),
            models.Index(fields=['make_and_model']),
            models.Index(fields=['tracking_status']),
            models.Index(fields=['vehicle_reg_no',
                         'tracking_status', 'asset_status', 'make_and_model']),
        ]


class AssetRegister(models.Model):
    asset = models.ForeignKey(Asset, on_delete=models.CASCADE)
    client = models.ForeignKey(
        Client, on_delete=models.CASCADE, null=True, blank=True)
    loan = models.ForeignKey(
        Loan, on_delete=models.CASCADE, null=True, blank=True)
    remedial = models.ForeignKey(
        Remedial, on_delete=models.CASCADE, null=True, blank=True)

    def __str__(self) -> str:
        return self.asset.vehicle_reg_no

    """For these statuses data, we will use requests to fetch them from CAMTOOL or wherever it is it comes from"""

    @property
    def main_status(self):
        # response = get_post_data(self.asset.vehicle_reg_no)
        # if response is not None:
        #     return response['main_status']
        return "NA"

    @property
    def backup_status(self):
        # response = get_post_data(self.asset.vehicle_reg_no)
        # if response is not None:
        #     return response['backup_status']
        return "NA"

    @property
    def location(self):
        # response = get_post_data(self.asset.vehicle_reg_no)
        # if response is not None:
        #     return response['location']
        return "NA"
