# Generated by Django 4.1.3 on 2022-11-22 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0017_alter_contactus_mobile_number_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='coin',
            name='type',
            field=models.CharField(choices=[('Bitcoin', 'Bitcoin'), ('Etherium', 'Etherium'), ('Cardano', 'Cardano'), ('BNB', 'BNB'), ('USDT', 'USDT')], max_length=8),
        ),
    ]