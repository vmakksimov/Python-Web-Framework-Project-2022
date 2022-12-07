# Generated by Django 4.1.3 on 2022-11-25 19:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0032_alter_coin_coin_prices'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='coin_prices',
            field=models.IntegerField(blank=True, choices=[('23049', '23049'), ('1515', '1515'), ('285', '285'), ('90', '90'), ('6', '6'), ('63', '63')], null=True),
        ),
        migrations.AlterField(
            model_name='coin',
            name='fiat_value',
            field=models.FloatField(blank=True, null=True),
        ),
    ]