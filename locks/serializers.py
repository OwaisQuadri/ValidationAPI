from rest_framework import serializers
from .models import Lock

#define ser class
class LockSerializer (serializers.ModelSerializer):
    #images must be posted using base64 encoding
    class Meta:
        model = Lock
        fields = ['name','status']
class LockPostSerializer (serializers.ModelSerializer):
    #images must be posted using base64 encoding
    class Meta:
        model = Lock
        fields = '__all__'
        