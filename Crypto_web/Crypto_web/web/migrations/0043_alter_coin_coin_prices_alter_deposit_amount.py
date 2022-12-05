# Generated by Django 4.1.3 on 2022-11-27 15:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0042_remove_deposit_bic_swift_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='coin_prices',
            field=models.IntegerField(blank=True, choices=[('Solana', '96'), ('Bitcoin', '22178'), ('Ethereum', '1792'), ('BNB', '346'), ('Polkadot', '10'), ('Dash', '108')], null=True),
        ),
        migrations.AlterField(
            model_name='deposit',
            name='amount',
            field=models.FloatField(blank=True, default=0, max_length=7, null=True),
        ),
    ]
