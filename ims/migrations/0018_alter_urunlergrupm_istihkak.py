# Generated by Django 3.2 on 2021-04-13 15:53

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0017_alter_urunlergrupm_istihkak'),
    ]

    operations = [
        migrations.AlterField(
            model_name='urunlergrupm',
            name='istihkak',
            field=models.BooleanField(default=False, verbose_name='İstihkak Ürünü'),
        ),
    ]