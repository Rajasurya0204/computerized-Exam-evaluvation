import cv2
import sys
import pytesseract

def image2text(image):   
	# Read image path from command line
	imPath = image

	# Define config parameters.
	# '-l eng'  for using the English language
	# '--oem 1' for using LSTM OCR Engine
	config = ('-l eng --oem 1 --psm 3')

	# Read image from disk
	im = cv2.imread(imPath, cv2.IMREAD_COLOR)

	# Run tesseract OCR on image
	text = pytesseract.image_to_string(im, config=config)

	# Print recognized text
	return text