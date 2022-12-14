# Generated by Django 4.1.3 on 2022-12-05 02:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0061_alter_deposit_options_alter_coin_coin_prices_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='coin_prices',
            field=models.IntegerField(blank=True, choices=[('Solana', 20), ('Bitcoin', 16505), ('Ethereum', 1178), ('BNB', 372), ('Polkadot', 14), ('Dash', 44), ('Avalanche', 66)], null=True),
        ),
        migrations.AlterField(
            model_name='coin',
            name='coin_prices_two',
            field=models.PositiveSmallIntegerField(choices=[(16505, 'Bitcoin'), (1178, 'Ethereum'), (372, 'Solana'), (20, 'BNB'), (14, 'Polkadot'), (44, 'Dash'), (66, 'Avalanche')], default=1),
        ),
    ]
