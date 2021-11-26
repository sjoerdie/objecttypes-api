# Generated by Django 2.2.24 on 2021-11-26 16:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0016_objecttype_has_geometry"),
    ]

    operations = [
        migrations.AlterField(
            model_name="objecttype",
            name="has_geometry",
            field=models.BooleanField(
                default=True,
                help_text="Shows whether the related objects have geographic coordinates. If the value is 'false' the related objects are not allowed to have coordinates and the creation/update of objects with `geometry` property will raise an error ",
                verbose_name="has geometry",
            ),
        ),
    ]
