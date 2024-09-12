from datetime import date
from django.db import models
from django.utils import timezone

# Create your models here.


class Remedial(models.Model):
    tracking_vendor = models.CharField(max_length=200)
    repossession_vendor = models.CharField(max_length=200)
    date_of_repossession = models.DateField(default=date.today)
    history_log = models.TextField()

    def __str__(self) -> str:
        return f"Remedial with Tracking from {self.tracking_vendor} and repossessor agent {self.repossession_vendor}"
