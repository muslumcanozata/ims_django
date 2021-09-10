from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

textLength = 255

class itemTransactionsM(models.Model):
    sku = models.IntegerField(verbose_name='SKU', validators=[MaxValueValidator(99999), MinValueValidator(10000)], null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    amount = models.FloatField(verbose_name='Adet', null=False, blank=False)
    iotype = models.BooleanField(verbose_name='İşlem Türü', null=False, blank=False)
    ds = models.CharField(verbose_name='Açıklama', max_length=textLength, null=False, blank=False)

    def __str__(self):
        return self.sku

    class Meta:
         db_table = "itemTransactionsM"
         verbose_name_plural = "Ürün Hareketleri"
         verbose_name = "Ürün Hareketi"