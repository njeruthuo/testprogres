# Generated by Django 5.1.1 on 2024-09-11 10:09

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('remedial', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='remedial',
            name='date_of_repossession',
            field=models.DateField(default=datetime.date.today),
        ),
    ]
