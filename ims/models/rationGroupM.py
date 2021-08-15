from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator

length = 45
textLength = 255
cinsiyetLength = 1

cinsiyetChoices = [
    ('E', 'Erkek'),
    ('K', 'Kadın')
]

class rationGroupM(models.Model):
    sku = models.IntegerField(verbose_name='SKU', unique=True, null=False, blank=False)
    group = models.IntegerField(verbose_name='İstihkak Grubu', null=False, blank=False)
    productGroup = models.CharField(verbose_name='Ürün Grubu', max_length=length, null=True, blank=False)
    size = models.CharField(verbose_name='Beden', max_length=length, null=False, blank=False)
    frequency = models.BigIntegerField(verbose_name = "Frekans", validators=[MaxValueValidator(365), MinValueValidator(1)], null=False, blank=False)
    directorate = models.IntegerField(verbose_name='Müdürlük No', validators=[MinValueValidator(1), MaxValueValidator(100)], null=False, blank=False)
    gender = models.CharField(max_length=cinsiyetLength, choices=cinsiyetChoices, null=False, blank=False)
    ds = models.CharField(verbose_name='Not', max_length=textLength, blank=True, null=True)

    class Meta:
        db_table = "rationGroupM"
        verbose_name_plural = "İstihkak Grupları"
        verbose_name = "İstihkak Grubu"

    def __str__(self):
        return str(self.sku)