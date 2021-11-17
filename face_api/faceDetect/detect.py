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
        # initialize recognized
        recognized = ""
        # load image to save
        FMR=settings.MEDIA_ROOT
        # head=os.path.dirname(settings.BASE_DIR)+ imagesDir# fixes when system changes
        # get faces of random pic input
        input_image_path=FMR / str(Face.objects.last().face)
        input_image = fr.load_image_file(input_image_path)
        known_faces=Face.objects.filter(known=True)
        # get faces from input
        input_locations = fr.face_locations(input_image)
        numOfInputs = len(input_locations)
        count = 0
        input_encodings = fr.face_encodings(input_image,known_face_locations=input_locations)
        self.delete_unknowns()
        # get face encoding of knowns
        print ("Known users:")
        for f in known_faces:
            name_of_known = str(f.name)
            print(name_of_known)
            known_path=FMR / str(f.face)
            image_of_known = fr.load_image_file(known_path)
            known_face_encoding = fr.face_encodings(image_of_known)[0]
            
            for i in input_encodings:
                match = fr.compare_faces(known_face_encoding, i)
                
                if match == True:
                    print("recognized!")
                    output+= name_of_known+","
        try:
            if output[-1]==",":
                output=output[:-1]
        except:
            output=""
        return output
    def delete_unknowns(self):
        unknowns=Face.objects.filter(known=False)
        for this in unknowns:
            this.face.delete()
        unknowns.delete()
        #numOfFaces = len(facelocations)
        # if(numOfFaces > 1):
        #   print(f'there are {numOfFaces} faces in this image')
        # loop through face locations


        # recieves a picture with a mode [save, predict]

        # if save, save picture to the 'known' folder
        # else save to 'input' folder and run facialrecog against the picture in comparison to the known folder
