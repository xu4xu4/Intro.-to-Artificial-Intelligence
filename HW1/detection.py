import os
import cv2
import matplotlib.pyplot as plt

def detect(dataPath, clf):
    """
    Please read detectData.txt to understand the format. Load the image and get
    the face images. Transfer the face images to 19 x 19 and grayscale images.
    Use clf.classify() function to detect faces. Show face detection results.
    If the result is True, draw the green box on the image. Otherwise, draw
    the red box on the image.
      Parameters:
        dataPath: the path of detectData.txt
      Returns:
        No returns.
    """
    # Begin your code (Part 4)
    #raise NotImplementedError("To be implemented")
    element=[]
    f=open(dataPath, 'r')
    for line in f.readlines():
        element.append(line.split())
    temp=0
    while temp < len(element):
        image_name,number=map(str,element[temp])
        image=cv2.imread('data/detect/'+image_name)
        gray_image=cv2.imread('data/detect/'+image_name,cv2.IMREAD_GRAYSCALE)
        temp+=1
        final=[]
        for i in range(int(number)):
            final.append(list(map(int,element[temp])))
            temp+=1
        for face in final:
            left=face[0]
            top=face[1]
            right=face[0]+face[2]
            bottom=face[1]+face[3]
            face_image=cv2.resize(gray_image[top:bottom,left:right],(19,19),interpolation=cv2.INTER_LANCZOS4)
            if clf.classify(face_image)==1:
                cv2.rectangle(image,(left,top),(right,bottom),(0,255,0),thickness=5)
            else:
                cv2.rectangle(image,(left,top),(right,bottom),(0,0,255),thickness=5)
        cv2.imwrite('ans/tt/'+image_name,image)        
            
    

    # End your code (Part 4)
