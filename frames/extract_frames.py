from os import listdir
import cv2

for file in listdir('/home/divyanshs/Documents/arpit major final/FaceNet_FR-master/avi'):
    path = "/home/divyanshs/Documents/arpit major final/FaceNet_FR-master/avi/"+file
    camera = cv2.VideoCapture(path)
    i = 0
    
    while True:
        ret, frame = camera.read()
        if not ret: break
        i += 1
        if i%5: continue
        # frame = cv2.rotate(frame,cv2.ROTATE_180)
        cv2.imwrite("/home/divyanshs/Documents/arpit major final/FaceNet_FR-master/frames"+file.split(".")[0]+str(i)+'.jpg',frame)

        