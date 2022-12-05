# Generated by Django 4.1.3 on 2022-11-14 05:03

import Crypto_web.web.validators
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('web', '0005_addhelparticle'),
    ]

    operations = [
        migrations.CreateModel(
            name='HelpArticle',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=30)),
                ('name', models.CharField(max_length=10)),
                ('image', models.URLField()),
                ('description', models.TextField(blank=True, max_length=1000, null=True, validators=[Crypto_web.web.validators.validate_alphabet_characters_english])),
                ('date_created', models.DateField(auto_now_add=True)),
                ('author', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Help Article',
            },
        ),
    ]
