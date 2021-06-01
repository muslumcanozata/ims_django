# Generated by Django 3.2.3 on 2021-06-01 20:46

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0002_personellerm_rfid2'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='urunlergrupm',
            name='sku',
        ),
        migrations.AddField(
            model_name='istihkaklargrupm',
            name='urunGrup',
            field=models.CharField(max_length=45, null=True, verbose_name='Ürün Grubu'),
        ),
        migrations.AddField(
            model_name='personellerm',
            name='tel2',
            field=models.IntegerField(null=True, unique=True, validators=[django.core.validators.MaxValueValidator(5999999999), django.core.validators.MinValueValidator(5000000000)], verbose_name='Telefon (5012345678)'),
        ),
        migrations.AddField(
            model_name='urunlergrupm',
            name='frekans',
            field=models.BigIntegerField(null=True, validators=[django.core.validators.MaxValueValidator(365), django.core.validators.MinValueValidator(1)], verbose_name='Frekans'),
        ),
        migrations.AddField(
            model_name='urunlergrupm',
            name='mudurluk',
            field=models.IntegerField(null=True, validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Müdürlük No'),
        ),
        migrations.AlterField(
            model_name='personellerm',
            name='tel',
            field=models.CharField(max_length=10, unique=True, verbose_name='Telefon (05012345678)'),
        ),
    ]
