from rest_framework import status
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from ims.models import sarfKullanicilarM
from ims.api.serializers import sarfKullanicilarSerializer

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