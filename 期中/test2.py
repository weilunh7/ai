import cv2
import pytesseract
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator
import torch

model = YOLO('C:\\Users\\user\\Desktop\\Plates\\best.pt')

cap = cv2.VideoCapture('C:\\Users\\user\\Desktop\\Plates\\test.mp4')

while True:
    ret, frame = cap.read()
    results = model.predict(frame)

    for r in results:
        annotator = Annotator(frame)
        boxes = r.boxes

        for box in boxes:
            # 裁剪車牌區域
            x1, y1, x2, y2 = box.xyxy[0]
            x1 = int(x1)
            x2 = int(x2)
            y1 = int(y1)
            y1 = int(y2)
            print(x1,x2,y1,y2)
            plate = frame[y1:y2, x1:x2]
            
            # 使用 OCR 讀取車牌文字
            plate_text = pytesseract.image_to_string(plate)
            print("Detected Plate Text:", plate_text)
            
            # 在原始影像上顯示檢測結果和文字
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            cv2.putText(frame, plate_text, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.9, (36,255,12), 2)
    
    # 顯示結果影像
    cv2.imshow('Video', frame)
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()