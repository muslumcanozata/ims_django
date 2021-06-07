from django.urls import path
from ims.api import views as api_views
from .views import urunHareketListCreateAPIView, current_user, personellerRFDetailsListCreateAPIView, personellerQRDetailsListCreateAPIView, personellerListCreateAPIView, userList

urlpatterns = [
    path('sarfKullanicilar/', api_views.sarfKullanicilarListCreateAPIView.as_view(), name='Sarf Kullanıcılar Listesi'),
    path('sarfKullanicilar/<int:pk>', api_views.sarfKullanicilarDetailsListCreateAPIView.as_view(), name='Sarf Kullanıcılar Detay Listesi'),
    path('personeller/', api_views.personellerListCreateAPIView.as_view(), name="Personel Bilgileri"),
    path('personellerQR/<int:tel2>/', api_views.personellerQRDetailsListCreateAPIView.as_view(), name="Personel Detay Bilgileri"),
    path('personellerRF/<int:rfid2>/', api_views.personellerRFDetailsListCreateAPIView.as_view(), name="Urun Hareket Bilgileri"),
    path('urunTeslim/', api_views.urunTeslimViews.as_view(), name="Alınabilecek Ürün Bilgileri"),
    path('urunHareketler/', api_views.urunHareketListCreateAPIView.as_view(), name="Personel Bilgileri"),
    path('current_user/', current_user),
    path('users/', userList.as_view())
]
