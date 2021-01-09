import cv2
import numpy as np
import face_recognition
import os

path = 'ImagesAttendance'
images = []
classNames = []
myList = os.listdir(path)
print(myList)
for cls in myList:
    curImg = cv2.imread(f'{path}/{cls}')
    images.append(curImg)
    classNames.append(os.path.splitext(cls)[0])
print(classNames)

def findEncodings(images):
    encodeList = []
    for img in images:
        img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)




# 2nd step
# faceLoc = face_recognition.face_locations(img)[0]
# encodeElon = face_recognition.face_encodings(img)[0]
# cv2.rectangle(img, (faceLoc[3], faceLoc[0]), (faceLoc[1], faceLoc[2]), (255, 0, 255), 2)
#
# faceLocTest = face_recognition.face_locations(imgTest)[0]
# encodeTest = face_recognition.face_encodings(imgTest)[0]
# cv2.rectangle(imgTest, (faceLocTest[3], faceLocTest[0]), (faceLocTest[1], faceLocTest[2]), (255, 0, 255), 2)
#
#  # 3rd step
# results = face_recognition.compare_faces([encodeElon], encodeTest)
# faceDis = face_recognition.face_distance([encodeElon], encodeTest)



#1st step
# imgElon = face_recognition.load_image_file('ImagesBasic/musk2.jpg')
# #convert to rgb
# imgElon = cv2.cvtColor(imgElon,cv2.COLOR_BGR2RGB)
# imgTest = face_recognition.load_image_file('ImagesBasic/elon-test.jfif')
# imgTest = cv2.cvtColor(imgTest, cv2.COLOR_BGR2RGB)