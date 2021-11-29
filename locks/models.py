from django.db import models
from django.conf import settings
import os

# Create your models here.
class Lock (models.Model):
    lock_name = models.CharField(max_length=100,blank=True,null=True)
    status = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name