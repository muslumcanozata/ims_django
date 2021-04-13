from django.db import models 

textLength = 255

class istihkakM(models.Model):
    grup = models.IntegerField(verbose_name='İstihkak Grubu', unique=True, primary_key=True, null=False, blank=False)
    ds = models.CharField(verbose_name='Tanım', max_length=textLength, null=False, blank=False)

    def __str__(self):
        return self.ds

    class Meta:
         db_table = "İstihkak"
         verbose_name_plural = "İstihkaklar"
         verbose_name = "İstihkak"