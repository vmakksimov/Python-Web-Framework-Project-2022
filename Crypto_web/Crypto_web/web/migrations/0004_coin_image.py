# Generated by Django 4.1.3 on 2022-11-13 03:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0003_remove_coin_stable_coin_quantity'),
    ]

    operations = [
        migrations.AddField(
            model_name='coin',
            name='image',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
