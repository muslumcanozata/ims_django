# Generated by Django 3.2 on 2021-04-13 17:26

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0021_urunhareketlerm'),
    ]

    operations = [
        migrations.CreateModel(
            name='istihkaklarGrupM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sku', models.IntegerField(unique=True, verbose_name='SKU')),
                ('grup', models.IntegerField(verbose_name='İstihkak Grubu')),
                ('beden', models.CharField(max_length=45, verbose_name='Beden')),
                ('frekans', models.BigIntegerField(validators=[django.core.validators.MaxValueValidator(365), django.core.validators.MinValueValidator(1)], verbose_name='Frekans')),
                ('mudurluk', models.IntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(100)], verbose_name='Müdürlük No')),
                ('cinsiyet', models.CharField(choices=[('E', 'Erkek'), ('K', 'Kadın')], max_length=1)),
                ('ds', models.CharField(blank=True, max_length=255, null=True, verbose_name='Not')),
            ],
            options={
                'verbose_name': 'İstihkak Grubu',
                'verbose_name_plural': 'İstihkak Grupları',
                'db_table': 'İstihkak Grupları',
            },
        ),
    ]