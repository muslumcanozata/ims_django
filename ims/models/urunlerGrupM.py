from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

length = 45
textLength = 255

class urunlerGrupM(models.Model):
    isim = models.CharField(verbose_name='Ürün İsmi', max_length=length, null=False, blank=False)
    istihkak = models.BooleanField(verbose_name='İstihkak Ürünü', default=False, null=False, blank=False)
    grup = models.IntegerField(verbose_name='İstihkak Grubu', blank=True)
    # sku = models.IntegerField(verbose_name='SKU', unique=True, null=False, blank=False)
    mudurluk = models.IntegerField(verbose_name='Müdürlük No', validators=[MinValueValidator(1), MaxValueValidator(100)], null=True, blank=False)
    frekans = models.BigIntegerField(verbose_name = "Frekans", validators=[MaxValueValidator(365), MinValueValidator(1)], null=True, blank=False)
    ds = models.CharField(verbose_name='Not', max_length=textLength, blank=True, null=True)

    class Meta:
        db_table = "ÜrünlerGrup Bilgileri"
        verbose_name_plural = "ÜrünlerGrup Bilgileri"
        verbose_name = "ÜrünlerGrup Bilgisi"

    def __str__(self):
        return self.isim
