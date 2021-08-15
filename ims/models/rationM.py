from django.db import models 

textLength = 255

class rationM(models.Model):
    group = models.IntegerField(verbose_name='İstihkak Grubu', unique=True, primary_key=True, null=False, blank=False)
    r_name = models.CharField(verbose_name='Tanım', max_length=textLength, null=False, blank=False)

    def __str__(self):
        return self.r_name

    class Meta:
         db_table = "rationM"
         verbose_name_plural = "İstihkaklar"
         verbose_name = "İstihkak"