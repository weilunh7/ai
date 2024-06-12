import cv2
import pytesseract
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator

model = YOLO('C:\\Users\\user\\Desktop\\Plates\\best.pt')
cap = cv2.VideoCapture('C:\\Users\\user\\Desktop\\Plates\\test.mp4')

while True:
  ret, frame = cap.read()
  results = model.predict(frame)
  for r in results:
    annotator = Annotator(frame)
    boxes = r.boxes
    for box in boxes:
        b = box.xyxy[0]  # get box coordinates in (left, top, right, bottom) format
        c = box.cls
        annotator.box_label(b, model.names[int(c)])
    frame = annotator.result()
    cv2.imshow('test',frame)
  if cv2.waitKey() & 0xFF == ord('q'):
      break

cap.release()
cv2.destroyAllWindows()