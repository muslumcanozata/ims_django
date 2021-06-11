from django.urls import path
from ims.api import views as api_views
from .views import urunHareketListCreateAPIView, current_user, personellerRFDetailsListCreateAPIView, personellerQRDetailsListCreateAPIView, personellerFaceDetailsListCreateAPIView, personellerListCreateAPIView, userList, Home, FaceDetect, GrupDetailsRetrieveUpdateAPIView, MudurlukDetailsRetrieveUpdateAPIView


urlpatterns = [
    path('sarfKullanicilar/', api_views.sarfKullanicilarListCreateAPIView.as_view(), name='Sarf Kullanıcılar Listesi'),
    path('sarfKullanicilar/<int:pk>', api_views.sarfKullanicilarDetailsListCreateAPIView.as_view(), name='Sarf Kullanıcılar Detay Listesi'),
    path('personeller/', api_views.personellerListCreateAPIView.as_view(), name="Personel Bilgileri"),
    path('personellerQR/<int:tel>/', api_views.personellerQRDetailsListCreateAPIView.as_view(), name="Personel Detay Bilgileri"),
    path('personellerRF/<slug:rfid>/', api_views.personellerRFDetailsListCreateAPIView.as_view(), name="Urun Hareket Bilgileri"),
    path('personellerFace/<int:isno>/', api_views.personellerFaceDetailsListCreateAPIView.as_view(), name="Urun Hareket Bilgileri"),
    path('urunTeslim/', api_views.urunTeslimViews.as_view(), name="Alınabilecek Ürün Bilgileri"),
    path('urunHareketler/', api_views.urunHareketListCreateAPIView.as_view(), name="Personel Bilgileri"),
    path('current_user/', current_user),
    path('users/', userList.as_view()),
    path('face_detect/', Home),
    path('user_face_detect/', FaceDetect),
    path('istihkakgrup/<slug:grup>', api_views.GrupDetailsRetrieveUpdateAPIView.as_view(), name='İstihkakGrup'),
    path('mudurluk/<slug:mudurluk>', api_views.MudurlukDetailsRetrieveUpdateAPIView.as_view(), name='Mudurluk')
]
