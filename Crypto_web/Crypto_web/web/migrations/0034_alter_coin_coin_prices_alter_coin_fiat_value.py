# Generated by Django 4.1.3 on 2022-11-25 19:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0033_alter_coin_coin_prices_alter_coin_fiat_value'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='coin_prices',
            field=models.IntegerField(blank=True, choices=[('17981', '17981'), ('2472', '2472'), ('361', '361'), ('171', '171'), ('12', '12'), ('47', '47')], null=True),
        ),
        migrations.AlterField(
            model_name='coin',
            name='fiat_value',
            field=models.FloatField(blank=True, max_length=1000000, null=True),
        ),
    ]