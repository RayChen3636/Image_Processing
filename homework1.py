# 寫一個可以自動幫圖片加上浮水印的程式。
# 程式要可以設定浮水印的內容、大小與呈現方式(自定義)
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

m1_input = input("請輸入執行檔檔名:")
content = input("請輸入內容:")
size = input("請輸內容入大小:")

m1 = cv2.imread(m1_input, 1)

# 圖像高
d = m1.shape[0]
print("圖像高:",d)
# 圖像寬
e = m1.shape[1]
print("圖像寬:", e)

m2 = Image.fromarray(m1)
tf = ImageFont.truetype("kaiu.ttf", int(size))
ImageDraw.Draw(m2).text((e/2-int(size)/4*len(content),d/2 -int(size)/2) , content , (125,125,125),tf)
m1 = np.array(m2)

cv2.imshow("Image_1", m1)
cv2.waitKey(0)
cv2.destroyAllWindows()