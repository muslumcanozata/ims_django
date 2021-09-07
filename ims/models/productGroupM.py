from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

length = 45
textLength = 255

class productGroupM(models.Model):
    name = models.CharField(verbose_name='Ürün İsmi', max_length=length, null=False, blank=False)
    group = models.IntegerField(verbose_name='İstihkak Grubu', blank=True)
    piece = models.FloatField(verbose_name='Alınabilecek Adet', null=True, blank=False)
    directorate = models.IntegerField(verbose_name='Müdürlük No', validators=[MinValueValidator(1), MaxValueValidator(100)], blank=False)
    frequency = models.BigIntegerField(verbose_name = "Frekans", validators=[MaxValueValidator(730), MinValueValidator(1)], blank=False)
    isRation = models.BooleanField(verbose_name='İstihkak Ürünü', default=False, null=False, blank=False)
    ds = models.CharField(verbose_name='Not', max_length=textLength, blank=True, null=True)

    class Meta:
        db_table = "productGroupM"
        verbose_name_plural = "ÜrünlerGrup Bilgileri"
        verbose_name = "ÜrünlerGrup Bilgisi"

    def __str__(self):
        return self.name
