# Generated by Django 4.1.3 on 2022-11-22 02:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0011_newsletter_remove_contactus_newsletter'),
    ]

    operations = [
        migrations.AddField(
            model_name='contactus',
            name='newsletter',
            field=models.EmailField(default=1, max_length=254),
            preserve_default=False,
        ),
    ]
