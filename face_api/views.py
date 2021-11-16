from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from .models import Face
from .serializers import FaceSerializer
from .faceDetect.detect import Detect
import os
from django.conf import settings
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

class FaceAPIView (APIView):
    #get for seeing who is registered (return names and picture of who is known)
    def get(self,request):
        faces=Face.objects.all()
        ser=FaceSerializer(faces,many=True)
        
        return Response(ser.data)
    #post for checking if there is a known user in picture posted (return username or 'Unregistered User')
    #@csrf_exempt
    def post(self,request):
        faceDetector=Detect()
        ser = FaceSerializer(data = request.data)
        if ser.is_valid():
            ser.save()
            #check if posted img is known or unknown
            last=Face.objects.last()
            known=last.known
            output="Nobody was recognized"
            if not known:
                #if unknown use faceDetector and check for user within known files
                output=faceDetector.recognize()
                print("\noutput: ",output)
            else:
                output="known user added"
                print(output)
                print("known users are:")
                for user in Face.objects.all():
                    print(user.name)
            return Response(output, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    


class DeleteFaceAPIView(APIView):
    def get(self,request,name):
        # name=name.replace("%20"," ")
        if name is "null":
            name=""
        face=Face.objects.filter(name=name)
        for f in face:
            f.face.delete()
        face.delete()
        if name is "null":
            name=""
        face=Face.objects.filter(name=name)
        for f in face:
            f.face.delete()
        face.delete()
        return Response(status = status.HTTP_204_NO_CONTENT)
        


    