from django.db import models

# Create your models here.
class Face (models.Model):
    name = models.CharField(max_length=100)
    face = models.ImageField(upload_to='images')
    known = models.BooleanField()
    date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name