from django.db import models
from assets.models import Client


class LoanStatus(models.Model):
    loan_status = models.CharField(max_length=50)
    is_deleted = models.BooleanField(default=False)
    client = models.ForeignKey(
        Client, models.CASCADE, related_name='loan_status', null=False)
    pass
    """
    loan_status_id integer NOT NULL,
    loan_status character varying NOT NULL,
    is_deleted boolean DEFAULT false NOT NULL,
    client_id integer DEFAULT '-1'::integer NOT NULL
    """
