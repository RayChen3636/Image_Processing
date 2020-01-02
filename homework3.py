import cv2
import numpy as np
from PIL import ImageFont, ImageDraw, Image

c = cv2.VideoCapture("homework3.mp4")

while True:
    r, m1 = c.read()
    # m3 = np.full(m1.shape, (255, 255, 255), np.uint8)
    if r == True:
        m2 = cv2.inRange(m1, (91, 0, 0), (190, 160, 100))
        m2 = cv2.blur(m2, (5, 5))
        # m2 = cv2.morphologyEx( m2, cv2.MORPH_GRADIENT, np.ones((30,30)))

        # m2 = cv2.medianBlur( m2, 3)
        # m2 = cv2.bitwise_not(m2)
        m2 = cv2.erode(m2,
                       np.ones((3, 3))
                       )
        m2 = cv2.dilate(m2,
                        np.ones((10, 10))
                        )


        # m2 = cv2.dilate(m2,
        #                 np.ones((40,40))
        #                 )

        # m2 = cv2.morphologyEx( m1, cv2.MORPH_GRADIENT, np.ones((5,5)))
        # m2 = cv2.cvtColor(m2, cv2.COLOR_BGR2GRAY)
        # m2 = cv2.dilate(m2, np.ones((5, 5)))

        # m2 = cv2.erode( m2, np.ones((2,2)))

        # m2 = cv2.equalizeHist(m1)



        # m2 = cv2.medianBlur( m1,11)


        t1, m2 = cv2.threshold(m2, 130, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)

        c1, t1 = cv2.findContours(m2, cv2.RETR_TREE, cv2.CHAIN_APPROX_NONE)
        print(c1)
        print(t1)
        # x, y, w, h = cv2.boundingRect(c1[1])
        # cv2.rectangle(m1, (x, y), (x + w, y + h), (0, 0, 255), 2)
        for i in range(1, len(c1)):
            x, y, w, h = cv2.boundingRect(c1[i])
            if  w > 60 and h > 30:
                cv2.rectangle(m1, (x, y), (x + w, y + h), (0, 0, 255), 2)
                cv2.imshow("Image_1", m1)

        # cv2.imshow("Image_1", m1)
        cv2.imshow("Image_2", m2)
        cv2.waitKey(3)
    else:
        break
cv2.destroyAllWindows()