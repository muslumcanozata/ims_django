# Generated by Django 3.2 on 2021-06-02 22:33

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0006_auto_20210601_2259'),
    ]

    operations = [
        migrations.RenameField(
            model_name='istihkakm',
            old_name='ds',
            new_name='i_isim',
        ),
        migrations.RenameField(
            model_name='mudurlukm',
            old_name='ds',
            new_name='m_isim',
        ),
    ]
