# 車牌辨識使用YOLOv8+EasyOCR
## 在Colab上訓練YOLOv8
[Yolov8訓練Colab連結](https://colab.research.google.com/drive/1424vL3lo8Kp7ebcPzBUb2cdHOaLxm-XB)

## 心得
在研究車牌辨識時，最初的想法是結合YOLO和pytesseract進行辨識。不過我遇到了無法裁切YOLO偵測到的圖片的問題，並且發現在圖片歪斜的情況下pytesseract效果不佳。此外，當使用Annotator進行文字標記時也出現了問題，後來發現是因為使用`cv2.VideoCapture`時源視頻的分辨率過高所導致的問題。

經過研究YOLO的裁切功能和OCR技術後，我決定使用easyocr進行車牌文字的辨識，期間也嘗試了形態學技術，但最終選擇了使用easyocr，因為設定相對簡單。最終的成果在`final.py`中，不過在過程中遇到了`result[0] out of range`的錯誤，一開始在網上找不到相關信息，最後發現是因為沒有偵測到圖片的問題。

實際顯示文字的問題還要解決，當圖片變換太快的話會來不及顯示，但文字是有偵測到並儲存到檔案標題的。

## 參考資料
- YOLO參數設定：[How to Detect Objects in Images using YOLOv8](https://www.freecodecamp.org/news/how-to-detect-objects-in-images-using-yolov8/)
- 裁切技術：[Ultralytics Object Cropping Guide](https://docs.ultralytics.com/zh/guides/object-cropping/#visuals)
- OCR技術：[Geek CSDN OCR Guide](https://geek.csdn.net/658a81a0dafaf23eeaee3b9c.html?dp_token=eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpZCI6NTAxMDg2OSwiZXhwIjoxNzE4NzgzNTE4LCJpYXQiOjE3MTgxNzg3MTgsInVzZXJuYW1lIjoid2VpbHVuaDcifQ.cw0hcbXWUMGZGVH6dWhLFOJhPd2LEyIzEqA-_d3TybE)
- EasyOCR：[EasyOCR車牌辨識](https://chtseng.wordpress.com/2020/11/04/%E5%8B%95%E6%85%8B%E8%BB%8A%E7%89%8C%E8%BE%A8%E8%AD%98%E8%88%87easyocr/)
- OpenCV錯誤解決：[CSDN OpenCV Error Resolution](https://blog.csdn.net/tsyccnh/article/details/102915803)
- OpenCV相關技術：
  - [OpenCV Text Handling](https://steam.oxxostudio.tw/category/python/ai/opencv-text.html)
  - [OpenCV Write Image](https://steam.oxxostudio.tw/category/python/ai/opencv-write-image.html)
## Youtube 展示
 https://youtu.be/ZMQFTu6qdkI
