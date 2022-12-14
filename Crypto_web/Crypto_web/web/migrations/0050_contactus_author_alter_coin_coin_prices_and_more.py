# Generated by Django 4.1.3 on 2022-11-28 14:36

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0049_alter_coin_coin_prices_alter_coin_coin_prices_two_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='author',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='coin',
            name='coin_prices',
            field=models.IntegerField(blank=True, choices=[('Solana', 75), ('Bitcoin', 16479), ('Ethereum', 1523), ('BNB', 367), ('Polkadot', 5), ('Dash', 61), ('Avalanche', 75)], null=True),
        ),
        migrations.AlterField(
            model_name='coin',
            name='coin_prices_two',
            field=models.PositiveSmallIntegerField(choices=[(16479, 'Bitcoin'), (1523, 'Ethereum'), (367, 'Solana'), (75, 'BNB'), (5, 'Polkadot'), (61, 'Dash'), (75, 'Avalanche')], default=1),
        ),
    ]
