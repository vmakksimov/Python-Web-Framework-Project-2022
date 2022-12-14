# Generated by Django 4.1.3 on 2022-11-29 16:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0052_alter_coin_coin_prices_alter_coin_coin_prices_two'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='cvv',
            field=models.CharField(default=1, max_length=3),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='coin',
            name='iban',
            field=models.CharField(default=1, max_length=11),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coin',
            name='card_number',
            field=models.CharField(default=1, max_length=20),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coin',
            name='coin_prices',
            field=models.IntegerField(blank=True, choices=[('Solana', 71), ('Bitcoin', 16871), ('Ethereum', 1273), ('BNB', 298), ('Polkadot', 14), ('Dash', 53), ('Avalanche', 62)], null=True),
        ),
        migrations.AlterField(
            model_name='coin',
            name='coin_prices_two',
            field=models.PositiveSmallIntegerField(choices=[(16871, 'Bitcoin'), (1273, 'Ethereum'), (298, 'Solana'), (71, 'BNB'), (14, 'Polkadot'), (53, 'Dash'), (62, 'Avalanche')], default=1),
        ),
        migrations.AlterField(
            model_name='coin',
            name='payment_method',
            field=models.CharField(choices=[('Visa', 'Visa'), ('MasterCard', 'MasterCard')], max_length=10),
        ),
    ]
