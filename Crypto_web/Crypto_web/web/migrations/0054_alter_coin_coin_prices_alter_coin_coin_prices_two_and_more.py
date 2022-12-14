# Generated by Django 4.1.3 on 2022-11-29 16:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0053_coin_cvv_coin_iban_alter_coin_card_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='coin_prices',
            field=models.IntegerField(blank=True, choices=[('Solana', 94), ('Bitcoin', 16181), ('Ethereum', 1646), ('BNB', 344), ('Polkadot', 11), ('Dash', 65), ('Avalanche', 85)], null=True),
        ),
        migrations.AlterField(
            model_name='coin',
            name='coin_prices_two',
            field=models.PositiveSmallIntegerField(choices=[(16181, 'Bitcoin'), (1646, 'Ethereum'), (344, 'Solana'), (94, 'BNB'), (11, 'Polkadot'), (65, 'Dash'), (85, 'Avalanche')], default=1),
        ),
        migrations.AlterField(
            model_name='coin',
            name='cvv',
            field=models.CharField(max_length=3, verbose_name='CVV'),
        ),
        migrations.AlterField(
            model_name='coin',
            name='iban',
            field=models.CharField(max_length=11, verbose_name='IBAN'),
        ),
    ]
