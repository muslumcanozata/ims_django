# Generated by Django 3.2 on 2021-04-13 00:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0012_skum'),
    ]

    operations = [
        migrations.CreateModel(
            name='istihkakM',
            fields=[
                ('grup', models.IntegerField(primary_key=True, serialize=False, unique=True, verbose_name='İstihkak Grubu')),
                ('ds', models.CharField(max_length=255, verbose_name='Tanım')),
            ],
            options={
                'verbose_name': 'İstihkak',
                'verbose_name_plural': 'İstihkaklar',
                'db_table': 'İstihkak',
            },
        ),
    ]
