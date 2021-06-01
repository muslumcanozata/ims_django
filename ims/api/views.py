from django.http import HttpResponseRedirect
from rest_framework import permissions, status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.serializers import Serializer
from django.contrib.auth.models import User
from ims.models import sarfKullanicilarM
from ims.api.serializers import sarfKullanicilarSerializer, userSerializer, userSerializerWithToken

#for class views
from rest_framework.views import APIView
from rest_framework.generics import get_object_or_404


#face detect
from ims.FACE_DETECT.deepface2.DeepFace import stream
from django.http import HttpResponse


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


@api_view(['GET'])
def Home(request):
    try:
        cam = VideoCamera() 
        result = gen(cam)
    except:
        result = "None"
        pass
    return HttpResponse(result)


class VideoCamera(object):
    
    def get_frame(object):
        result = stream("ims/FACE_DETECT/FaceImages",model_name ='Dlib',time_threshold = 1, frame_threshold = 5)
        print(result,"Kisisi tespit edildi")
        return result


def gen(cam):
    return cam.get_frame()
        
