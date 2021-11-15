from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from .models import Face
from .serializers import FaceSerializer
from .faceDetect.detect import Detect

# Create your views here.

class FaceAPIView (APIView):
    #get for seeing who is registered (return names and picture of who is known)
    def get(self,request):
        faces=Face.objects.all()
        ser=FaceSerializer(faces,many=True)
        faceDetector=Detect()
        faceDetector.recognize()
        return Response(ser.data)
    #post for checking if there is a known user in picture posted (return username or 'Unregistered User')
    def post(self,request):
        ser = FaceSerializer(data = request.data)

        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    def delete_unknowns(self):
        unknowns=Face.objects.filter(known=False).delete()

class DeleteFaceAPIView(APIView):
    def get(self,request,name):
        face=Face.objects.filter(name=name)
        face.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        


    