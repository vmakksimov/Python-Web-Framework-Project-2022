# Generated by Django 4.1.3 on 2022-11-13 02:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='stable',
            field=models.BooleanField(),
        ),
    ]
