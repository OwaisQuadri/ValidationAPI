# facial recognition implementation
import face_recognition as fr
from PIL import Image
import os
from os import path
import urllib.request as request
from django.conf import settings
from ..models import Face
import socket
from io import BytesIO


# face_recognition --tolderance .40 ./known ./input
class Detect:
    def __init__(self):
        pass
    def recognize(self):
        #init output
        output=""
        # load image to save
        FMR=settings.MEDIA_ROOT
        # head=os.path.dirname(settings.BASE_DIR)+ imagesDir# fixes when system changes
        # get faces of random pic input
        input_image_path=FMR / str(Face.objects.last().face)
        input_image = fr.load_image_file(input_image_path)
        known_faces=Face.objects.filter(known=True)
        # get faces from input
        input_locations = fr.face_locations(input_image)
        input_encodings = fr.face_encodings(input_image,known_face_locations=input_locations)
        self.delete_unknowns()
        # get face encoding of knowns
        for f in known_faces:
            name_of_known = str(f.name)
            known_path=FMR / str(f.face)
            image_of_known = fr.load_image_file(known_path)
            
            try:
                #if someone in the known picture
                known_face_encoding = fr.face_encodings(image_of_known)[0]
                matches = fr.compare_faces(known_face_encoding, input_encodings)
                for match in matches:
                    if match == True:
                        #recognized
                        output+= name_of_known+","
            except:
                continue
            
        try:
            if output[-1]==",":
                output=output[:-1]
        except:
            return ""
        return output
    def delete_unknowns(self):
        unknowns=Face.objects.filter(known=False)
        for this in unknowns:
            this.face.delete()
        unknowns.delete()
        unknowns=Face.objects.filter(name=None)
        for this in unknowns:
            this.face.delete()
        unknowns.delete()
