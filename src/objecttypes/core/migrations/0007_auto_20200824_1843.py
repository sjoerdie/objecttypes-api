# Generated by Django 2.2.12 on 2020-08-24 16:43

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("core", "0006_auto_20200902_1706"),
    ]

    operations = [
        migrations.AlterField(
            model_name="objectversion",
            name="publication_date",
            field=models.DateField(
                default=datetime.date.today,
                help_text="Date of Version publication",
                verbose_name="publication date",
            ),
        ),
    ]
