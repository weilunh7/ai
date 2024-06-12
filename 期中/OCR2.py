import easyocr
import cv2 as cv

reader = easyocr.Reader(['ch_sim','en'])
"""""
src = cv.imread('output.jpg')
gray = cv.cvtColor(src,cv.COLOR_BGR2GRAY)
ret,binary = cv.threshold(gray,0,255,cv.THRESH_BINARY_INV| cv.THRESH_OTSU)
kernel = cv.getStructuringElement(cv.MORPH_RECT,(1,2))  #去除横向细线
morph1 = cv.morphologyEx(binary,cv.MORPH_OPEN,kernel)
kernel = cv.getStructuringElement(cv.MORPH_RECT, (2, 1)) #去除纵向细线
morph2 = cv.morphologyEx(morph1,cv.MORPH_OPEN,kernel)
cv.bitwise_not(morph2,morph2)
"""""
result = reader.readtext('output.jpg',detail=0)

print(result)