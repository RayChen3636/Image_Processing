# 剔除指定照片上除文字以外的景物
import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

m1 = cv2.imread("g1.png", 1)
m2 = cv2.inRange(m1, (0,0,255), (255,255,255))
# m2 = m2  - 255
m2 =cv2.bitwise_not(m2)

cv2.imshow("Image_1", m1)
cv2.imshow("Image_2", m2)
cv2.waitKey(0)
cv2.destroyAllWindows()
