from rest_framework import serializers
from django.contrib.auth.models import User
from rest_framework_jwt.settings import api_settings
from ims.models import sarfKullanicilarM, personellerM

class sarfKullanicilarSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = sarfKullanicilarM
        fields = '__all__'

class personellerSerializer(serializers.ModelSerializer):
    
    class Meta:
        model = personellerM
        fields = '__all__'

class userSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ('username',)
class userSerializerWithToken(serializers.ModelSerializer):

    token = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True)

    def get_token(self,obj):
        jwt_payload_handler = api_settings.JWT_PAYLOAD_HANDLER
        jwt_encode_handler = api_settings.JWT_ENCODE_HANDLER
    
        payload = jwt_payload_handler(obj)
        token = jwt_encode_handler(payload)

    def create(self,validated_data):
        password = validated_data.pop('password', None)
        instance = self.Meta.model(**validated_data)

        if password is not None:
            instance.set_password(password)
        instance.save()
        return instance
    
    class Meta:
        model = User
        fields = ('token', 'username', 'password')