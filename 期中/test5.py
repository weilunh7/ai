import os
import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
import pytesseract

model = YOLO('C:\\Users\\user\\Desktop\\Plates\\car.pt')
names = model.names
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
cap = cv2.VideoCapture('C:\\Users\\user\\Desktop\\test.png')

idx = 0
while cap.isOpened():
    success, im0 = cap.read()
    cv2.namedWindow("im0", 0)
    cv2.resizeWindow("im0", 480, 270)
    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break

    results = model.predict(im0, show=False)
    boxes = results[0].boxes.xyxy.cpu().tolist()
    clss = results[0].boxes.cls.cpu().tolist()
    annotator = Annotator(im0, line_width=2, example=names)

    if boxes is not None:
        for box, cls in zip(boxes, clss):
            idx += 1
            if(names[int(cls)] == "license-plate"):
                crop_obj = im0[int(box[1]) : int(box[3]), int(box[0]) : int(box[2])]
                plate_text = pytesseract.image_to_string(crop_obj)
                annotator.box_label(box,label=plate_text,color=colors(int(cls), True))

    cv2.imshow("im0", im0)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()