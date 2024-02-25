import cv2
import numpy as np
import matplotlib.pyplot as plt


image = cv2.imread('test_img.jpg') #returns image as numpy array
lane_image = np.copy(image)

gray = cv2.cvtColor(lane_image, cv2.COLOR_RGB2GRAY)
blur = cv2.GaussianBlur(gray, (3, 3), 0) #Args: image, kernel size, deviation; the canny function acc automatically does this for us
canny = cv2.Canny(blur, 70, 400)#Args: image, low threshold, high threshold


plt.imshow(canny) #can also use cv2 instead of plt
plt.show()
#cv2.waitKey(0)