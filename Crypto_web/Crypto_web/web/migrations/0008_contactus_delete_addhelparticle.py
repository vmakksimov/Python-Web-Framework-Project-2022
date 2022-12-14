# Generated by Django 4.1.3 on 2022-11-14 15:39

import Crypto_web.web.validators
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0007_remove_helparticle_author'),
    ]

    operations = [
        migrations.CreateModel(
            name='ContactUs',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('mobile_number', models.IntegerField(validators=[Crypto_web.web.validators.validate_if_number_starts_with_country_code, django.core.validators.MaxLengthValidator(12), django.core.validators.MinLengthValidator(10, message='The number is incorrect.')])),
                ('email', models.EmailField(max_length=254)),
                ('message', models.TextField()),
                ('newsletter', models.EmailField(blank=True, max_length=254, null=True)),
            ],
            options={
                'verbose_name': 'Contact Us',
            },
        ),
        migrations.DeleteModel(
            name='AddHelpArticle',
        ),
    ]
