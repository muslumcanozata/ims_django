from django.contrib import admin
from ims.models import (
    sarfKullanicilarM, personellerM, mudurlukM
)

# Register your models here.

@admin.register(sarfKullanicilarM)
class sarfKullanicilarMAdmin(admin.ModelAdmin):
    search_fields = (
        'isno', 'isim', 'soyisim', 'email', 'tel'
        )
    list_display = (
        'isno', 'isim', 'soyisim', 'tel'
    )

@admin.register(personellerM)
class personellerMAdmin(admin.ModelAdmin):
    search_fields = (
        'isno', 'isim', 'soyisim', 'email', 'tel', 'rfid', 'mudurluk', 'ilkamirlik', 'grup'
    )
    list_display = (
        'isno', 'isim', 'soyisim', 'email', 'tel', 'mudurluk', 'ilkamirlik'
    )

@admin.register(mudurlukM)
class mudurlukM(admin.ModelAdmin):
    search_fields = (
        'mudurluk', 'ds'
        )
    list_display = (
        'ds', 'mudurluk'
    )