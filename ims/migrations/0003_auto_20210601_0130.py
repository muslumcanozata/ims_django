# Generated by Django 3.2 on 2021-05-31 22:30

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0002_personellerm_rfid2'),
    ]

    operations = [
        migrations.AddField(
            model_name='personellerm',
            name='tel2',
            field=models.IntegerField(null=True, unique=True, validators=[django.core.validators.MaxValueValidator(5000000000), django.core.validators.MinValueValidator(5000000000)], verbose_name='Telefon (5012345678)'),
        ),
        migrations.AlterField(
            model_name='personellerm',
            name='tel',
            field=models.CharField(max_length=10, unique=True, verbose_name='Telefon (05012345678)'),
        ),
    ]