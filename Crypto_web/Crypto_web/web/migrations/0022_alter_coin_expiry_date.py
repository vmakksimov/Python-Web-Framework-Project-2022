# Generated by Django 4.1.3 on 2022-11-24 04:26

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0021_coin_cvv_coin_expiry_date_coin_network_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='expiry_date',
            field=models.DateField(blank=True, default=django.utils.timezone.now, null=True),
        ),
    ]
