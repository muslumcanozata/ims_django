# Generated by Django 3.2 on 2021-05-23 18:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='personellerm',
            name='rfid2',
            field=models.CharField(max_length=12, null=True, verbose_name='rfid2'),
        ),
    ]