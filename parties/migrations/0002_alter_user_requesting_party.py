# Generated by Django 4.1.7 on 2023-04-12 19:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("parties", "0001_initial"),
    ]

    operations = [
        migrations.AlterField(
            model_name="user",
            name="Requesting_party",
            field=models.BooleanField(default=True, verbose_name="Requesting Party"),
        ),
    ]
