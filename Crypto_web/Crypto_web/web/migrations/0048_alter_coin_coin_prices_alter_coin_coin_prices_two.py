# Generated by Django 4.1.3 on 2022-11-28 02:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0047_alter_coin_coin_prices_alter_coin_coin_prices_two'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='coin_prices',
            field=models.IntegerField(blank=True, choices=[('Solana', 28), ('Bitcoin', 16375), ('Ethereum', 1381), ('BNB', 306), ('Polkadot', 12), ('Dash', 82)], null=True),
        ),
        migrations.AlterField(
            model_name='coin',
            name='coin_prices_two',
            field=models.PositiveSmallIntegerField(choices=[(16375, 'Bitcoin'), (1381, 'Ethereum'), (306, 'Solana'), (28, 'BNB'), (12, 'Polkadot'), (82, 'Dash')], default=1),
        ),
    ]
