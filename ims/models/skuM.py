from django.db import models

textLength = 255

class skuM(models.Model):
    sku = models.IntegerField(verbose_name='SKU', unique=True, primary_key=True, null=False, blank=False)
    ds = models.CharField(verbose_name='Tanım', max_length=textLength, null=False, blank=False)

    def __str__(self):
        return self.ds

    class Meta:
         db_table = "skuM"
         verbose_name_plural = "SKU Bilgileri"
         verbose_name = "SKU Bilgisi"