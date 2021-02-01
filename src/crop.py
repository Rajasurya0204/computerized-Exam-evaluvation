import cv2
import imutils
import numpy as np
from main import rec


def getKey(image):
	# reading the image
	kernel = np.ones((5,5),np.uint8)
	img = cv2.imread(image)
	#display the image
	#cv2.namedWindow("Origi", cv2.WINDOW_NORMAL )
	# cv2.imshow("Origi",img)
	# cv2.waitKey(0)

	#grey-scaling and dilating
	gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
	gray = 255*(gray < 100).astype(np.uint8) 
	dilation = cv2.dilate(gray,kernel,iterations = 20)
	
	# finding countours/boundaries in the images
	im2, contours, hierarchy = cv2.findContours(dilation, cv2.RETR_TREE, cv2.CHAIN_APPROX_SIMPLE)
	cv2.destroyAllWindows()

	# Segmenting the image
	kwords=[]
	idx = 0
	for c in contours:
		x,y,w,h = cv2.boundingRect(c)
		if w>50 and h>50:
			idx+=1
			new_img=img[y:y+h,x:x+w]
			new_img = cv2.erode(new_img,kernel,iterations = 1)
			cv2.imwrite('../data/' + str(idx) + '.png', new_img)
			kwords.append(rec('../data/' + str(idx) + '.png'))
	print(kwords)
	return kwords