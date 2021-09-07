from django.db import models
from ims.models import employeeM, userM, productGroupM

length = 12
class pendingProductM(models.Model):
    desired = models.FloatField(verbose_name='İstenilen Adet', null=False, blank=False)
    date = models.DateTimeField(auto_now_add=True)
    emp_isno = models.ForeignKey(employeeM, on_delete=models.CASCADE)
    user_isno = models.ForeignKey(userM, on_delete=models.CASCADE)
    product_id = models.ForeignKey(productGroupM, on_delete=models.CASCADE)
    order_id = models.CharField(verbose_name='Sipariş Numarası', max_length=length, null=False, blank=False)

    class Meta:
        db_table = "pendingProductM"
        verbose_name_plural = "Bekleyen Ürünler"
        verbose_name = "Bekleyen Ürün"

    def __str__(self):
        return str(self.emp_isno)