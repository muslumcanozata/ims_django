from ims.models.urunHareketlerM import urunHareketlerM
from ims.models.urunlerGrupM import urunlerGrupM
from ims.models.personellerM import personellerM
from django.http import HttpResponseRedirect
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from django.contrib.auth.models import User
from ims.models import sarfKullanicilarM
from ims.api.serializers import personellerSerializer, sarfKullanicilarSerializer, urunHareketSerializer, urunlerGrupSerializer, userSerializer, userSerializerWithToken
#genericsAPIView
from rest_framework.generics import GenericAPIView
from rest_framework import generics

#for class views
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


#face detect
from ims.FACE_DETECT.deepface2.DeepFace import stream
from ims.FACE_DETECT.face_detection import face_detect
from django.http import HttpResponse

from django.db import connection


from django.http import JsonResponse




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

class personellerFaceDetailsListCreateAPIView(generics.RetrieveUpdateAPIView):
    queryset = personellerM.objects.all()
    serializer_class = personellerSerializer
    lookup_field = 'isno'



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

#face_detect#

@api_view(['GET'])
def Home(request):
    try:
        cam = VideoCamera() 
        result = gen(cam)
        #silinecek daha sonra
        result = "22222"
    except:
        result = "0"
        pass
    result = int(result)
    return JsonResponse({'isno': result})


@api_view(['GET'])
def FaceDetect(request, isno=None):
    if not isno:
        isno = request.GET.get('isno', '')

        if(face_detect(isno)):
            return JsonResponse({'result':1})

    return JsonResponse({'result': 0})


class VideoCamera(object):
    
    def get_frame(object):
        result = stream("ims/FACE_DETECT/FaceImages",model_name ='Dlib',time_threshold = 1, frame_threshold = 5)
        print(result,"Kisisi tespit edildi")
        return result


def gen(cam):
    return cam.get_frame()
 #face_detect#   

class urunTeslimViews(APIView):

    def get(self, request):
        print(request.GET.get('isno'))
        isno = request.GET.get('isno')
        cursor = connection.cursor()
        raw_query = '''select ug.id, ug.isim, ug.adet
                    from 'ÜrünlerGrup Bilgileri' as ug
                    left join 'Ürün Hareketleri' as uh on ug.id = uh.urun_id_id
                            and uh.id = (
                                    select uhs.id 
                                    from 'Ürün Hareketleri' as uhs 
                                    where uhs.urun_id_id = uh.urun_id_id and uhs.per_isno_id = %s
                                    order by uhs.tarih desc
                                    limit 1)
                    where (ug.mudurluk, ug.grup) In ( select mudurluk, grup
                                                from Personeller  
                                                where isno = %s)
                            and (uh.per_isno_id is null
                            or ug.frekans <= cast(julianday('now') - julianday(uh.tarih) as integer))'''
        return Response(cursor.execute(raw_query, [isno, isno]))

class urunHareketListCreateAPIView(generics.ListCreateAPIView):
    queryset = urunHareketlerM.objects.all()
    serializer_class = urunHareketSerializer
