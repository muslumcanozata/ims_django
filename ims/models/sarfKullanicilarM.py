from django.db import models
from django.db.models import Model
from django.core.validators import MaxValueValidator, MinValueValidator

length = 45
phoneLength = 10
textLength = 255

class sarfKullanicilarM(models.Model):
    isno = models.IntegerField(verbose_name='İş Numarası', primary_key=True, validators=[MaxValueValidator(99999), MinValueValidator(10000)], unique=True, null=False, blank=False)
    email = models.EmailField(verbose_name='Email Adresi', unique=True, null=False, blank=False)
    isim = models.CharField(verbose_name='İsim', max_length=length, null=False, blank=False)
    soyisim = models.CharField(verbose_name='Soyisim', max_length=length, null=False, blank=False)
    tel = models.CharField(verbose_name='Telefon (5012345678)', max_length=phoneLength, unique=True, null=False, blank=False)
    ds = models.CharField(verbose_name='Not', max_length=textLength, blank=True)

    def __str__(self):
        return self.isim + " " + self.soyisim

    class Meta:
        db_table = "Sarf Kullanıcılar"
        verbose_name_plural = "Sarf Kullanıcılar"
        verbose_name = "Sarf Kullanıcı"
