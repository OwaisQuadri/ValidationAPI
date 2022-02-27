from posixpath import split
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
from rq import Queue
from .worker import conn

# Create your views here.
class FaceAPIView(APIView):
    # get for seeing who is registered (return names and picture of who is known)
    def get(self, request):
        faces = Face.objects.filter(known=True)
        ser = FaceSerializer(faces, many=True)
        return Response(ser.data)  # ser.data)

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
                q =Queue(connection=conn)
                # if unknown use faceDetector and check for user within known files
                names= q.enqueue('views.faceDetector.recognize')
                name=names.split(',')[0]
                if name=="":
                    return Response("", status=status.HTTP_201_CREATED)
                else:
                    faces = Face.objects.none()
                    for name in names:
                        faces|=Face.objects.filter(name=name)
                    recognized=FaceSerializer(faces,many=True )
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
