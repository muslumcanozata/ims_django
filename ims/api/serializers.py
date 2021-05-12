from rest_framework import serializers
from ims.models import sarfKullanicilarM

class sarfKullanicilarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = sarfKullanicilarM
        fields = '__all__'