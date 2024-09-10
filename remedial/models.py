from django.db import models

# Create your models here.


class Remedial(models.Model):
    tracking_vendor = models.CharField(max_length=200)
    repossession_vendor = models.CharField(max_length=200)
    date_of_repossession = models.DateField()
    history_log = models.TextField()

    def __str__(self) -> str:
        return f"Remedial with Tracking from {self.tracking_vendor} and repossessor agent {self.repossession_vendor}"
