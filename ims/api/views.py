from ims.models.personellerM import personellerM
from django.http import HttpResponseRedirect
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from django.contrib.auth.models import User
from ims.models import sarfKullanicilarM
from ims.api.serializers import personellerSerializer, sarfKullanicilarSerializer, userSerializer, userSerializerWithToken

#genericsAPIView
from rest_framework.generics import GenericAPIView
from rest_framework import generics

#for class views
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404

class sarfKullanicilarListCreateAPIView(APIView):
    def get(self, request):
        sarfKullanicilar = sarfKullanicilarM.objects.all()
        serializer = sarfKullanicilarSerializer(sarfKullanicilar, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = sarfKullanicilarSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class sarfKullanicilarDetailsListCreateAPIView(APIView):
    
    def get_object(self, pk):
        sarfKullanicilar_instance = get_object_or_404(sarfKullanicilarM, pk=pk)
        return sarfKullanicilar_instance
    
    def get(self, request, pk):
        sarfKullanicilar = self.get_object(pk=pk)
        serializer = sarfKullanicilarSerializer(sarfKullanicilar)
        return Response(serializer.data)

    def put(self, request, pk):
        sarfKullanicilar =self.get_object(pk=pk)
        serializer = sarfKullanicilarSerializer(sarfKullanicilar, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class personellerListCreateAPIView(APIView):
    def get(self, request):
        personeller = personellerM.objects.all()
        serializer = personellerSerializer(personeller, many=True)
        return Response(serializer.data)
    
    def post(self, request):
        serializer = personellerSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class personellerRFDetailsListCreateAPIView(generics.RetrieveUpdateAPIView):
    queryset = personellerM.objects.all()
    serializer_class = personellerSerializer
    lookup_field = 'rfid2'

class personellerQRDetailsListCreateAPIView(generics.RetrieveUpdateAPIView):
    queryset = personellerM.objects.all()
    serializer_class = personellerSerializer
    lookup_field = 'tel2'



#for login authentication
@api_view(['GET'])
def current_user(request):

    serializer = userSerializer(request.user)
    return Response(serializer.data)

class userList(APIView):

    permission_classes = (permissions.AllowAny,)

    def post(self, request, format=None):
        serializer = userSerializerWithToken(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)