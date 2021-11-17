from django.db import models
from django.conf import settings
import os
from uuid import uuid4

def path_and_rename(instance, filename):
    upload_to = 'images/known/'
    ext = filename.split('.')[-1]
    # get filename
    if instance.name:
        filename = '{}.{}'.format(instance.name, ext)
    else:
        # set filename as random string
        filename = '{}.{}'.format(uuid4().hex, ext)
    # return the whole path to the file
    return os.path.join(upload_to, filename)
# Create your models here.
class Face (models.Model):
    name = models.CharField(max_length=100,blank=True,null=True)
    face = models.ImageField(upload_to=path_and_rename)
    known = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name