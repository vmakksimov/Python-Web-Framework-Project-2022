# Generated by Django 3.2.9 on 2022-12-10 04:57

import Crypto_web.common.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='CryptoEvent',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100, validators=[Crypto_web.common.validators.validate_alphabet_characters_english])),
                ('description', models.CharField(max_length=200, validators=[Crypto_web.common.validators.validate_alphabet_characters_english])),
                ('is_event_of_month', models.BooleanField(default=False)),
                ('event_image', models.URLField()),
                ('event_date', models.DateField()),
            ],
            options={
                'verbose_name': 'Event',
            },
        ),
    ]