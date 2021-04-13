from django.db import models
from ims.models import personellerM

length = 45
textLength = 255

class bedenlerM(models.Model):
    grup = models.IntegerField(verbose_name='İstihkak Grubu', null=False, blank=False)
    beden = models.CharField(verbose_name='Beden', max_length=length, null=False, blank=False)
    isno = models.ForeignKey(personellerM, on_delete=models.CASCADE)
    ds = models.CharField(verbose_name='Not', max_length=textLength, blank=True)

    def __str__(self):
        return str(self.isno)
    
    class Meta:
        db_table = "Bedenler"
        verbose_name_plural = "Bedenler"
        verbose_name = "Beden"
    