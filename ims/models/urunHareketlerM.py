from django.db import models
from ims.models import personellerM, sarfKullanicilarM, urunlerGrupM

class urunHareketlerM(models.Model):
    verilenadet = models.FloatField(verbose_name='Verilen Adet', null=False, blank=False)
    istenilenadet = models.FloatField(verbose_name='İstenilen Adet', null=False, blank=False)
    tarih = models.DateTimeField(auto_now_add=True)
    per_isno = models.ForeignKey(personellerM, on_delete=models.CASCADE)
    kull_isno = models.ForeignKey(sarfKullanicilarM, on_delete=models.CASCADE)
    urun_id = models.ForeignKey(urunlerGrupM, on_delete=models.CASCADE)

    class Meta:
        db_table = "Ürün Hareketleri"
        verbose_name_plural = "Ürün Hareketleri"
        verbose_name = "Ürün Hareketi"

    def __str__(self):
        return str(self.per_isno)
