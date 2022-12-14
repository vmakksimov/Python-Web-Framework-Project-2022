# Generated by Django 4.1.3 on 2022-12-03 16:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0059_alter_coin_coin_prices_alter_coin_coin_prices_two'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='coin_prices',
            field=models.IntegerField(blank=True, choices=[('Solana', 32), ('Bitcoin', 16153), ('Ethereum', 1315), ('BNB', 275), ('Polkadot', 5), ('Dash', 84), ('Avalanche', 72)], null=True),
        ),
        migrations.AlterField(
            model_name='coin',
            name='coin_prices_two',
            field=models.PositiveSmallIntegerField(choices=[(16153, 'Bitcoin'), (1315, 'Ethereum'), (275, 'Solana'), (32, 'BNB'), (5, 'Polkadot'), (84, 'Dash'), (72, 'Avalanche')], default=1),
        ),
    ]
