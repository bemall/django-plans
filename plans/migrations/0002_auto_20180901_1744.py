# Generated by Django 2.0.8 on 2018-09-01 15:44

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("plans", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="order",
            name="plan_extended_from",
            field=models.DateField(
                blank=True,
                null=True,
                verbose_name="plan extended from",
                help_text="The plan was extended from this date",
            ),
        ),
        migrations.AddField(
            model_name="order",
            name="plan_extended_until",
            field=models.DateField(
                blank=True,
                null=True,
                verbose_name="plan extended until",
                help_text="The plan was extended until this date",
            ),
        ),
    ]
