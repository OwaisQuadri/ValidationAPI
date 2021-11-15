# facial recognition implementation
import face_recognition as fr
from PIL import Image
import os
from os import path
from ..models import Face
# face_recognition --tolderance .40 ./known ./input
class Detect:
    def __init__(self):
        pass
    def recognize(self):
        # initialize recognized
        recognized = ""
        # load image to save
        head="C:\\Users\\Owais\\Documents\\capstone\\validation-API\\ValidationAPI\\face_api\\faceDetect\\"
        knownPics = os.listdir(path.join(head,"known"))
        # get faces of random pic input
        input_image = fr.load_image_file(path.join(head,"input.png"))
        # get faces from input
        input_locations = fr.face_locations(input_image)
        numOfInputs = len(input_locations)
        count = 0
        for input in input_locations:
            count += 1
            top, right, bottom, left = input
            face_input = input_image[top:bottom, left:right]
            pil_image = Image.fromarray(face_input)
            # pil_image.show()
            pil_image.save(path.join(head,f'./input/input{count}.png'))
        # get face encoding of knowns
        print ("Known users:")
        for f in knownPics:
            name_of_known = f[:-4]
            print(name_of_known)
            image_of_known = fr.load_image_file(path.join(head,f'./known/{f}'))
            known_face_encoding = fr.face_encodings(image_of_known)[0]

            # compare current known against inputs
            inputLocation = os.listdir(path.join(head,"./input/"))
            print("\nUsers recognized in input.png:")
            for i in inputLocation:
                img = fr.load_image_file(path.join(head,f'./input/{i}'))
                face_encoding = fr.face_encodings(img)
                match = fr.compare_faces(known_face_encoding, face_encoding)[0]
                input_name = "Unknown Individual"
                if match == True:
                    recognized = name_of_known
                    print(f'{recognized} was recognized')


        #numOfFaces = len(facelocations)
        # if(numOfFaces > 1):
        #   print(f'there are {numOfFaces} faces in this image')
        # loop through face locations


        # recieves a picture with a mode [save, predict]

        # if save, save picture to the 'known' folder
        # else save to 'input' folder and run facialrecog against the picture in comparison to the known folder
