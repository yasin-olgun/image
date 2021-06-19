import cv2
import numpy as np

ellipse = np.array([[0, 0, 1, 0, 0],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [1, 1, 1, 1, 1],
       [0, 0, 1, 0, 0]], dtype=np.uint8)
images = ["1.jpg","2.jpg","3.jpg","4.jpg","5.jpg","6.jpg","7.jpg","8.jpg"]

for i in images:
    threshold1 = 100
    threshold2 = 250
    img = cv2.imread(i)
    img = cv2.pyrDown(img) #resmi küçültme
    edge=cv2.Canny(img.copy(),threshold1,threshold2)
    h,w=edge.shape
    count=0
    for j in range(0,h):
        for k in range(0,w):
            if edge[j][k]==255:
                count+=1
    ratio = (count/(h*w))*100 # deger cok kucuk oldugu icin 100 ile carptim
    if ratio>1 and ratio<8: # 1 ve 8 degerlerini kendim deneme yanilma yaparak en iyi oldugunu dusundugum degerleri sectim
        mask = cv2.dilate(edge.copy(),ellipse,iterations=4)
        restoredImg = cv2.inpaint(img.copy(),mask,3,cv2.INPAINT_TELEA)
        cv2.imwrite("restored"+i,restoredImg)
    elif ratio>8:
        mask = cv2.dilate(edge.copy(),ellipse,iterations=1)
        restoredImg = cv2.inpaint(img.copy(),mask,3,cv2.INPAINT_TELEA)
        cv2.imwrite("restored"+i,restoredImg)
    else:
        threshold1-=50
        threshold2-=50
        edge=cv2.Canny(img.copy(),threshold1,threshold2)
        mask = cv2.dilate(edge.copy(),ellipse,iterations=4)
        restoredImg = cv2.inpaint(img.copy(),mask,3,cv2.INPAINT_TELEA)
        cv2.imwrite("restored"+i,restoredImg)
        # cv2.imshow yerine imwrite kullandim, imshow ayni anda cok fazla resim actigi icin karsilastirma cok rahat
        # yapilamiyordu.
