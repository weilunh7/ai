import os
import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
import pytesseract
import numpy as np

model = YOLO('C:\\Users\\user\\Desktop\\Plates\\best.pt')
names = model.names
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
cap = cv2.VideoCapture('C:\\Users\\user\\Desktop\\Plates\\test2.mp4')

assert cap.isOpened(), "Error reading video file"
w, h, fps = (int(cap.get(x)) for x in (cv2.CAP_PROP_FRAME_WIDTH, cv2.CAP_PROP_FRAME_HEIGHT, cv2.CAP_PROP_FPS))

alpha = 1.7
beta = 0

crop_dir_name = "ultralytics_crop"
if not os.path.exists(crop_dir_name):
    os.mkdir(crop_dir_name)

# Video writer
    video_writer = cv2.VideoWriter("object_cropping_output.avi", cv2.VideoWriter_fourcc(*"mp4v"), fps, (w, h))

idx = 0
while cap.isOpened():
    success, im0 = cap.read()
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
            #annotator.box_label(box, color=colors(int(cls), True), label=names[int(cls)])
            if(names[int(cls)] == "license-plate"):
                crop_obj = im0[int(box[1]) : int(box[3]), int(box[0]) : int(box[2])]
                #adjusted1 = cv2.convertScaleAbs(crop_obj,alpha=alpha,beta=beta)
                #adjusted2 = cv2.cvtColor(adjusted1,cv2.COLOR_RGB2GRAY)
                #kernel = np.ones((5,5),np.uint8)
                #binary = cv2.dilate(adjusted2,kernel,iterations=2)
                #binary = cv2.dilate(binary,kernel,iterations=1)
                #ret,binary = cv2.threshold(binary,250,255,cv2.THRESH_BINARY)
                #plate_text = pytesseract.image_to_string(crop_obj)
                annotator.box_label(box,label=names[int(cls)],color=colors(int(cls), True))
                cv2.imwrite(os.path.join(crop_dir_name, str(idx) + ".png"), crop_obj)

    cv2.imshow("ultralytics", im0)
    video_writer.write(im0)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
video_writer.release()
cv2.destroyAllWindows()