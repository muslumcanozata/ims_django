from django.db import models
from ims.models import employeeM, userM, productGroupM

class givenProductM(models.Model):
    given = models.FloatField(verbose_name='Verilen Adet', null=False, blank=False)
    desired = models.FloatField(verbose_name='İstenilen Adet', null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    emp_isno = models.ForeignKey(employeeM, on_delete=models.CASCADE)
    user_isno = models.ForeignKey(userM, on_delete=models.CASCADE)
    product_id = models.ForeignKey(productGroupM, on_delete=models.CASCADE)

    class Meta:
        db_table = "givenProductM"
        verbose_name_plural = "Ürün Hareketleri"
        verbose_name = "Ürün Hareketi"

    def __str__(self):
        return str(self.emp_isno)
