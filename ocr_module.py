import cv2
import numpy as np
import easyocr

def preprocess_image(image):
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blur = cv2.bilateralFilter(gray, 11, 17, 17)
    edged = cv2.Canny(blur, 30, 200)
    return edged

def extract_text_from_image(image):
    reader = easyocr.Reader(['en'])
    result = reader.readtext(image)
    text = ' '.join([res[1] for res in result])
    return text
