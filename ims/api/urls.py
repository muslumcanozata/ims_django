from django.urls import path
from ims.api import views as api_views

urlpatterns = [
    path('sarfKullanicilar/', api_views.sarfKullanicilarListCreateAPIView.as_view(), name='Sarf Kullanıcılar Listesi'),
    path('sarfKullanicilar/<int:pk>', api_views.sarfKullanicilarDetailsListCreateAPIView.as_view(), name='Sarf Kullanıcılar Detay Listesi')
]
