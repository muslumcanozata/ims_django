from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

textLength = 255

class stocksM(models.Model):
    sku = models.IntegerField(verbose_name='SKU', validators=[MaxValueValidator(99999), MinValueValidator(10000)], unique=True, null=False, blank=False)
    amount = models.FloatField(verbose_name='Adet', null=False, blank=False)
    ds = models.CharField(verbose_name='Açıklama', max_length=textLength, null=False, blank=False)

    def __str__(self):
        return self.sku

    class Meta:
         db_table = "stocksM"
         verbose_name_plural = "Stok Bilgileri"
         verbose_name = "Stok Bilgisi"