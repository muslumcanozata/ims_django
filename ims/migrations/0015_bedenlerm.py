# Generated by Django 3.2 on 2021-04-13 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ims', '0014_fiyatm'),
    ]

    operations = [
        migrations.CreateModel(
            name='bedenlerM',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('grup', models.IntegerField(verbose_name='İstihkak Grubu')),
                ('beden', models.CharField(max_length=45, verbose_name='Beden')),
                ('ds', models.CharField(max_length=255, verbose_name='Not')),
                ('isno', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='ims.personellerm')),
            ],
            options={
                'verbose_name': 'Beden',
                'verbose_name_plural': 'Bedenler',
                'db_table': 'Bedenler',
            },
        ),
    ]