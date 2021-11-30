from django.shortcuts import render
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework.parsers import JSONParser
from .models import Lock
from .serializers import LockSerializer,LockPostSerializer
import os
from django.conf import settings
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated

# Create your views here.
#lock status's
class LockStatusDetail(APIView):
    #checking lock status
    def get(self, request,lock_name):
        lock = Lock.objects.filter(lock_name=lock_name).last()
        lock_status = LockSerializer(lock)
        return Response(lock_status.data)  # ser.data)

class LockStatus(APIView):
    def post(self, request):
        ser = LockPostSerializer(data=request.data)
        if ser.is_valid():
            ser.save()
            return Response(ser.data, status=status.HTTP_201_CREATED)
        return Response(ser.errors, status=status.HTTP_400_BAD_REQUEST)
    def get(self, request):
        locks=Lock.objects.none()
        T=Lock.objects.all()
        names=[]
        for t in T:
            if t.name not in names:
                names.append(t.name)
                locks|=Lock.objects.filter(pk=t.pk)
        

        ser=LockSerializer(locks, many=True)
        
        return Response(ser.data, status=status.HTTP_200_OK)