from django.db import models
from django.db.models import Model
from django.core.validators import MaxValueValidator, MinValueValidator

textLength = 255

class butceKoduM(models.Model):
    kod = models.IntegerField(verbose_name='Bütçe Kodu', validators=[MinValueValidator(1), MaxValueValidator(100)], unique=True, null=False, blank=False)
    mudurluk = models.IntegerField(verbose_name='Müdürlük', unique= True, validators=[MinValueValidator(1), MaxValueValidator(100)], null=False, blank = False)
    euro = models.FloatField(verbose_name='Euro', null=False, blank = False)
    ds = models.CharField(verbose_name='Tanım', max_length=textLength, blank=True)

    def __str__(self):
        return str(self.kod)
    
    class Meta:
        db_table = "Bütçe Kodları"
        verbose_name_plural = "Bütçe Kodları"
        verbose_name = "Bütçe Kodu"
