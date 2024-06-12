import os
import cv2
from ultralytics import YOLO
from ultralytics.utils.plotting import Annotator, colors
import easyocr

model = YOLO('C:\\Users\\user\\Desktop\\Plates\\best.pt')
names = model.names
reader = easyocr.Reader(['en'])
cap = cv2.VideoCapture('C:\\Users\\user\\Desktop\\Plates\\test.mp4')

def detect_text(img):
    result = reader.readtext(img,detail=0)
    if result and len(result[0]) > 5:  # 先檢查 result 是否非空，然後檢查第一個元素的長度
        text = result[0]
        cv2.putText(im0, text, (50,100), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0,0,255), 1, cv2.LINE_AA) # 將偵測文字放在左上角
        cv2.imwrite(f"picture//{text}.png", img) # save pictures
    else:
        print("無檢測")
    #if(len(result[0])>7):
        #text = result[0]
        #cv2.putText(im0, text, (50,100), cv2.FONT_HERSHEY_SIMPLEX, 2.5, (0,0,255), 1, cv2.LINE_AA)
        #cv2.imwrite(f"picture//{text}.png", img)

while cap.isOpened():
    success, im0 = cap.read()
    if not success:
        print("Video frame is empty or video processing has been successfully completed.")
        break

    results = model.predict(im0, show=False)
    boxes = results[0].boxes.xyxy.cpu().tolist()
    clss = results[0].boxes.cls.cpu().tolist()


    if boxes is not None:
        for box, cls in zip(boxes, clss):
            if(names[int(cls)] == "license-plate"):
                crop_obj = im0[int(box[1]) : int(box[3]), int(box[0]) : int(box[2])]
                detect_text(crop_obj)
                continue

    cv2.imshow("test",im0)

    if cv2.waitKey(1) & 0xFF == ord("q"):
        break

cap.release()
cv2.destroyAllWindows()