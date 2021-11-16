from rest_framework import serializers
from .models import Face
from drf_extra_fields.fields import Base64ImageField

#define ser class
class FaceSerializer (serializers.ModelSerializer):
    #images must be posted using base64 encoding
    face=Base64ImageField()
    class Meta:
        model = Face
        fields = '__all__'
        