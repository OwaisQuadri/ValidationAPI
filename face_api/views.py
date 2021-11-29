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
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
class FaceAPIView(APIView):
    # get for seeing who is registered (return names and picture of who is known)
    def get(self, request):
        faces = Face.objects.filter(known=True)
        ser = FaceSerializer(faces, many=True)
        output = ""
        for f in faces:

            output += str(f.name) + ","
        if len(output) != 0:
            output = output[:-1]
        return Response(output)  # ser.data)

    # post for checking if there is a known user in picture posted (return username or 'Unregistered User')

    def post(self, request):
        faceDetector = Detect()
        ser = FaceSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            # check if posted img is known or unknown
            last = Face.objects.last()
            known = last.known
            if not known:
                # if unknown use faceDetector and check for user within known files
                names= faceDetector.recognize().split(',')
                if names[0]=="":
                    return Response("", status=status.HTTP_201_CREATED)
                else:
                    recognized=FaceSerializer(Face.objects.filter(name=names))
                    return Response(recognized.data, status=status.HTTP_201_CREATED)
            else:
                if last.phone is None:
                    last.face.delete()
                    last.delete()
                    return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
                if last.name is None:
                    last.name = "Unnamed User"
                last_ser=FaceSerializer(last)
                return Response(last_ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)


class DeleteFaceAPIView(APIView):
    def get(self, request, name):
        user = request.user
        # name=name.replace("%20"," ")
        if name == "null":
            name = ""
        face = Face.objects.filter(name=name)
        for f in face:
            f.face.delete()
        face.delete()

        return Response(status=status.HTTP_204_NO_CONTENT)
