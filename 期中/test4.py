import os
import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
import pytesseract
import numpy as np

model = YOLO('C:\\Users\\user\\Desktop\\Plates\\best.pt')
names = model.names
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
font_scale = 1.5
font = cv2.FONT_HERSHEY_PLAIN

cap = cv2.VideoCapture('C:\\Users\\user\\Desktop\\Plates\\test.mp4')

if not cap.isOpened():
    cap =cv2.VideoCapture(0)
if not cap.isOpened():
    raise IOError("Cannot open video")
    
counter= 0
while True:
    ret,frame=cap.read()
    counter +=1
    results = model.predict(frame, show=False)
    boxes = results[0].boxes.xyxy.cpu().tolist()
    clss = results[0].boxes.cls.cpu().tolist()
    if ((counter%20)==0):
        imgH, imgW,_ = frame.shape
        x1,y1,w1,h1 = 0,0,imgH,imgW
        for box, cls in zip(boxes, clss):
            if(names[int(cls)] == "license-plate"):
                crop_obj = frame[int(box[1]) : int(box[3]), int(box[0]) : int(box[2])]
                imgchar = pytesseract.image_to_string(frame)
                x,y,w,h = int(box[1]), int(box[2]), int(box[3]), int(box[4])
                cv2.rectangle(frame, (x, imgH-y), (w,imgH-h), (0,0,255),3)
                    
                cv2.putText(frame, imgchar, (x1 + int(w1/50), y1 + int(h1/50)), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255,0,0), 2)
                
                font = cv2.FONT_HERSHEY_SIMPLEX

    cv2.imshow('Text Detection Tutorial',frame)
        
    if cv2.waitKey(2) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()