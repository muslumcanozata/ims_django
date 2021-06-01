from django.contrib import admin
from ims.models import (
    sarfKullanicilarM, personellerM, mudurlukM, butceKoduM, skuM, istihkakM, fiyatM, bedenlerM, urunlerGrupM, urunHareketlerM, istihkaklarGrupM
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
        'rfid2',
    )
    list_display = (
        'isno', 'isim', 'soyisim', 'email', 'tel', 'mudurluk', 'ilkamirlik'
    )

@admin.register(mudurlukM)
class mudurlukMAdmin(admin.ModelAdmin):
    search_fields = (
        'mudurluk', 'ds'
        )
    list_display = (
        'ds', 'mudurluk'
    )

@admin.register(butceKoduM)
class butceKoduMAdmin(admin.ModelAdmin):
    search_fields = (
        'kod','mudurluk', 'ds'
        )
    list_display = (
        'kod','mudurluk', 'euro', 'ds'
    )

@admin.register(skuM)
class skuMAdmin(admin.ModelAdmin):
    search_fields = (
        'sku', 'ds'
        )
    list_display = (
        'sku', 'ds'
    )

@admin.register(istihkakM)
class istihkakMAdmin(admin.ModelAdmin):
    search_fields = (
        'grup', 'ds'
        )
    list_display = (
        'grup', 'ds'
    )

@admin.register(fiyatM)
class fiyatMAdmin(admin.ModelAdmin):
    search_fields = (
        'sku', 'euro', 'ds'
        )
    list_display = (
        'sku', 'euro', 'ds'
    )

@admin.register(bedenlerM)
class bedenlerMAdmin(admin.ModelAdmin):
    search_fields = (
        'isno', 'grup', 'beden'
        )
    list_display = (
        'isno', 'grup', 'beden'
    )

@admin.register(urunlerGrupM)
class urunlerGrupMAdmin(admin.ModelAdmin):
    search_fields = (
        'isim',
        )
    list_display = (
        'isim', 'grup', 'istihkak', 'frekans', 'mudurluk',
    )

@admin.register(urunHareketlerM)
class urunHareketlerMAdmin(admin.ModelAdmin):
    search_fields = (
        'per_isno', 'tarih', 'urun_id'
        )
    list_display = (
        'per_isno', 'tarih', 'urun_id', 'verilenadet', 'istenilenadet', 'urun_id'
    )

@admin.register(istihkaklarGrupM)
class istihkaklarGrupMAdmin(admin.ModelAdmin):
    search_fields = (
        'sku', 'grup', 'beden', 'cinsiyet', 'frekans', 'mudurluk'
    )
    list_display = (
        'sku', 'grup', 'urunGrup', 'beden', 'cinsiyet', 'frekans', 'mudurluk', 'ds'
    )