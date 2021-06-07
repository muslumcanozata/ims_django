from django.db import models
from django.db.models import Model
from django.core.validators import MaxValueValidator, MinValueValidator

cinsiyetChoices = [
    ('E', 'Erkek'),
    ('K', 'Kadın')
]

length = 45
phoneLength = 10
textLength = 255
cinsiyetLength = 1

class personellerM(models.Model):
    isno = models.IntegerField(verbose_name='İş Numarası', primary_key=True, validators=[MaxValueValidator(99999), MinValueValidator(10000)], unique=True, null=False, blank=False)
    email = models.EmailField(verbose_name='Email Adresi', unique=True, null=False, blank=False)
    isim = models.CharField(verbose_name='İsim', max_length=length, null=False, blank=False)
    soyisim = models.CharField(verbose_name='Soyisim', max_length=length, null=False, blank=False)
    tel2 = models.IntegerField(verbose_name='Telefon (5012345678)', validators=[MaxValueValidator(5999999999), MinValueValidator(5000000000)], unique=True, null=True, blank=False)
    tel = models.CharField(verbose_name='Telefon (05012345678)', max_length=phoneLength, unique=True, null=False, blank=False)
    rfid2 = models.CharField(max_length=12, verbose_name='rfid2', null=True)
    rfid = models.BigIntegerField(verbose_name = "RFID", validators=[MaxValueValidator(99999999999), MinValueValidator(1)], null=False, blank=False)
    mudurluk = models.IntegerField(verbose_name='Müdürlük', unique= True, validators=[MaxValueValidator(100), MinValueValidator(1)], null=False, blank=False)
    ilkamirlik = models.CharField(verbose_name='İlk Amirlik', unique= True, max_length=length, null=False, blank=False)
    cinsiyet = models.CharField(max_length=cinsiyetLength, choices=cinsiyetChoices, null=False, blank=False)
    grup = models.CharField(verbose_name='Grup', unique= True, max_length=length, null=False, blank=False)
    ds = models.CharField(verbose_name='Not', max_length=textLength, blank=True, null=True)

    def __str__(self):
        return str(self.isno)

    class Meta:
        db_table = "Personeller"
        verbose_name_plural = "Personeller"
        verbose_name = "Personel"
