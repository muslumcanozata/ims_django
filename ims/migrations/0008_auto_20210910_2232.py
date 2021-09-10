# Generated by Django 2.1.15 on 2021-09-10 19:32

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0007_auto_20210910_2128'),
    ]

    operations = [
        migrations.AlterField(
            model_name='itemtransactionsm',
            name='sku',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(99999), django.core.validators.MinValueValidator(10000)], verbose_name='SKU'),
        ),
    ]
