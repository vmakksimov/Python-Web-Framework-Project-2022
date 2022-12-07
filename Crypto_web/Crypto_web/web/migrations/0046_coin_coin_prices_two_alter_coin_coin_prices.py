# Generated by Django 4.1.3 on 2022-11-28 00:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0045_alter_coin_coin_prices_alter_deposit_amount'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='coin_prices_two',
            field=models.PositiveSmallIntegerField(choices=[(1, 'Available to borrow'), (2, 'Borrowed by someone'), (3, 'Archived - not available anymore')], default=1),
        ),
        migrations.AlterField(
            model_name='coin',
            name='coin_prices',
            field=models.IntegerField(blank=True, choices=[('Solana', '93'), ('Bitcoin', '20124'), ('Ethereum', '1411'), ('BNB', '344'), ('Polkadot', '9'), ('Dash', '61')], null=True),
        ),
    ]