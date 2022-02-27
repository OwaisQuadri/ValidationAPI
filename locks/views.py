from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from .models import Lock
from .serializers import LockSerializer,LockPostSerializer

# Create your views here.
#logs
class LogsAPIView(APIView):
    def get(self,request):
        changedLocks=Lock.objects.filter(changed_by__isnull=False).order_by('-id')
        logs=LockPostSerializer(changedLocks,many=True)
        return Response(logs.data)
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
        L=Lock.objects.all()
        names=[]
        for l in reversed(L):
            if l.lock_name not in names:
                names.append(l.lock_name)
                locks|=Lock.objects.filter(pk=l.pk)
        

        ser=LockSerializer(locks, many=True)
        
        return Response(ser.data, status=status.HTTP_200_OK)