from django.contrib import admin
from ims.models import (
    userM, employeeM, directorateM, budgetCodeM, skuM, rationM, priceM, sizeM, productGroupM, givenProductM, rationGroupM, pendingProductM
)

# Register your models here.

@admin.register(userM)
class userMAdmin(admin.ModelAdmin):
    search_fields = (
        'isno', 'name', 'surname', 'email', 'tel'
    )
    list_display = (
        'isno', 'name', 'surname', 'email', 'tel'
    )

@admin.register(employeeM)
class employeeMAdmin(admin.ModelAdmin):
    search_fields = (
        'rfid',
    )
    list_display = (
        'isno', 'name', 'surname', 'email', 'tel', 'directorate', 'manager'
    )

@admin.register(directorateM)
class directorateMAdmin(admin.ModelAdmin):
    search_fields = (
        'directorate', 'd_name'
    )
    list_display = (
        'd_name', 'directorate'
    )

@admin.register(budgetCodeM)
class budgetCodeMAdmin(admin.ModelAdmin):
    search_fields = (
        'code','directorate', 'ds'
    )
    list_display = (
        'code','directorate', 'euro', 'ds'
    )

@admin.register(skuM)
class skuMAdmin(admin.ModelAdmin):
    search_fields = (
        'sku', 'ds'
    )
    list_display = (
        'sku', 'ds'
    )

@admin.register(rationM)
class rationMAdmin(admin.ModelAdmin):
    search_fields = (
        'group', 'r_name'
    )
    list_display = (
        'group', 'r_name'
    )

@admin.register(priceM)
class fiyatMAdmin(admin.ModelAdmin):
    search_fields = (
        'sku', 'euro', 'ds'
    )
    list_display = (
        'sku', 'euro', 'ds'
    )

@admin.register(sizeM)
class sizeMAdmin(admin.ModelAdmin):
    search_fields = (
        'isno', 'group', 'size'
    )
    list_display = (
        'isno', 'group', 'size'
    )

@admin.register(productGroupM)
class productGroupMAdmin(admin.ModelAdmin):
    search_fields = (
        'name',
    )
    list_display = (
        'name', 'group', 'frequency', 'directorate', 'piece', 'isRation',
    )

@admin.register(givenProductM)
class givenProductMAdmin(admin.ModelAdmin):
    search_fields = (
        'emp_isno', 'date', 'product_id'
        )
    list_display = (
        'emp_isno', 'date', 'product_id', 'given', 'desired', 'product_id'
    )

@admin.register(pendingProductM)
class pendingProductMAdmin(admin.ModelAdmin):
    search_fields = (
        'emp_isno', 'date', 'product_id'
        )
    list_display = (
        'emp_isno', 'date', 'product_id', 'desired', 'product_id'
    )


@admin.register(rationGroupM)
class rationGroupMAdmin(admin.ModelAdmin):
    search_fields = (
        'sku', 'group', 'size', 'gender', 'frequency', 'directorate'
    )
    list_display = (
        'sku', 'group', 'productGroup', 'size', 'gender', 'frequency', 'directorate', 'ds'
    )