# Generated by Django 3.2 on 2021-06-10 22:42

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0009_personellerm_faceid'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personellerm',
            name='faceid',
        ),
        migrations.RemoveField(
            model_name='personellerm',
            name='rfid2',
        ),
        migrations.RemoveField(
            model_name='personellerm',
            name='tel2',
        ),
        migrations.AlterField(
            model_name='personellerm',
            name='grup',
            field=models.CharField(max_length=45, verbose_name='Grup'),
        ),
        migrations.AlterField(
            model_name='personellerm',
            name='ilkamirlik',
            field=models.CharField(max_length=45, verbose_name='İlk Amirlik'),
        ),
        migrations.AlterField(
            model_name='personellerm',
            name='mudurluk',
            field=models.IntegerField(validators=[django.core.validators.MaxValueValidator(100), django.core.validators.MinValueValidator(1)], verbose_name='Müdürlük'),
        ),
        migrations.AlterField(
            model_name='personellerm',
            name='rfid',
            field=models.CharField(max_length=12, null=True, verbose_name='RFID'),
        ),
        migrations.AlterField(
            model_name='personellerm',
            name='tel',
            field=models.IntegerField(null=True, unique=True, validators=[django.core.validators.MaxValueValidator(5999999999), django.core.validators.MinValueValidator(5000000000)], verbose_name='Telefon Numarası'),
        ),
    ]
