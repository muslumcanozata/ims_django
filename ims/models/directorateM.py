from django.db import models
from django.db.models import Model
from django.core.validators import MaxValueValidator, MinValueValidator

textLength = 255

class directorateM(models.Model):
    directorate = models.IntegerField(verbose_name='Müdürlük No', unique= True, validators=[MinValueValidator(1), MaxValueValidator(100)], null=False, blank=False)
    d_name = models.CharField(verbose_name='Müdürlük İsmi', max_length=textLength, unique = True, null=False, blank = False)
    def __str__(self):
        return self.d_name
    
    class Meta:
        db_table = "directorateM"
        verbose_name_plural = "Müdürlükler"
        verbose_name = "Müdürlük"
