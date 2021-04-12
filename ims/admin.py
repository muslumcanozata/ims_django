from django.contrib import admin
from ims.models import (
    sarfKullanicilarM,
)

# Register your models here.

@admin.register(sarfKullanicilarM)
class sarfKullanicilarAdmin(admin.ModelAdmin):
    search_fields = (
        'isno', 'isim', 'soyisim', 'email', 'tel'
        )
    list_display = (
        'isno', 'isim', 'soyisim', 'tel'
    )