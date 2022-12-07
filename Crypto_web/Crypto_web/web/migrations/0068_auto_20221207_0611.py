# Generated by Django 3.2.9 on 2022-12-07 04:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0067_auto_20221207_0610'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='coin_prices',
            field=models.IntegerField(blank=True, choices=[('Solana', 71), ('Bitcoin', 16701), ('Ethereum', 1500), ('BNB', 329), ('Polkadot', 6), ('Dash', 48), ('Avalanche', 96)], null=True),
        ),
        migrations.AlterField(
            model_name='coin',
            name='coin_prices_two',
            field=models.PositiveSmallIntegerField(choices=[(16701, 'Bitcoin'), (1500, 'Ethereum'), (329, 'Solana'), (71, 'BNB'), (6, 'Polkadot'), (48, 'Dash'), (96, 'Avalanche')], default=1),
        ),
    ]