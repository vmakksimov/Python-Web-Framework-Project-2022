# Generated by Django 4.1.3 on 2022-11-30 03:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0056_delete_helparticle_alter_deposit_options_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='coin_prices',
            field=models.IntegerField(blank=True, choices=[('Solana', 19), ('Bitcoin', 16669), ('Ethereum', 1345), ('BNB', 338), ('Polkadot', 9), ('Dash', 76), ('Avalanche', 85)], null=True),
        ),
        migrations.AlterField(
            model_name='coin',
            name='coin_prices_two',
            field=models.PositiveSmallIntegerField(choices=[(16669, 'Bitcoin'), (1345, 'Ethereum'), (338, 'Solana'), (19, 'BNB'), (9, 'Polkadot'), (76, 'Dash'), (85, 'Avalanche')], default=1),
        ),
    ]
