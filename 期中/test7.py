from ultralytics import YOLO
from PIL import Image

model = YOLO("C:\\Users\\user\\Desktop\\Plates\\car.pt")  

results = model.predict("C:\\Users\\user\\Desktop\\test.png")

result = results[0]

#print(len(result.boxes))

for box in result.boxes:
    label = box.cls[0].item()
    cords = [round(x) for x in box.xyxy[0].tolist()]
    #x1,x2,y1,y2 = cords
    prob = box.conf[0].item()
    #print(x1,x2,y1,y2)
    #if(label == 1.0):
        #crop = result[x2 : y2, x1 : y1]
    #print(label)
    #print(cords)
    #print(prob)
print(result.plot()[:,:,::-1])
#Image.fromarray(result.plot()[:,:,::-1]).show()
Image.fromarray(result.plot()[:,:,::-1]).show()
