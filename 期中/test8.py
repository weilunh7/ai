import os
import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
from PIL import Image
import pytesseract

model = YOLO("C:\\Users\\user\\Desktop\\Plates\\car.pt")
names = model.names
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread("C:\\Users\\user\\Desktop\\test.png")
results = model.predict(img, show=False)
boxes = results[0].boxes.xyxy.cpu().tolist()
clss = results[0].boxes.cls.cpu().tolist()
annotator = Annotator(img, line_width=2, example=names)

if boxes is not None:
    for box, cls in zip(boxes, clss):
        annotator.box_label(box, color=colors(int(cls), True), label=names[int(cls)])
        if(names[int(cls)] == "license-plate"):
            crop_obj = img[int(box[1]) : int(box[3]), int(box[0]) : int(box[2])]
            plate_text = pytesseract.image_to_string(crop_obj)
            annotator.box_label(box,label=plate_text,color=colors(int(cls), True))
Image.fromarray(crop_obj).show()
cv2.imwrite('output.jpg', crop_obj)