# Generated by Django 4.1.3 on 2022-11-25 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0028_coin_coin_prices_alter_coin_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='coin_prices',
            field=models.IntegerField(choices=[('23486', '23486'), ('1693', '1693'), ('382', '382'), ('61', '61'), ('9', '9'), ('79', '79')]),
        ),
    ]
