import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = "/Users/rohit/Work/Python/softwares/tesseract/build/tesseract"

img = cv2.imread('../photos/ikeabill.jpg')
img = cv2.cvtColor(img,cv2.COLOR_BGR2RGB)

print(pytesseract.image_to_string(img))

cv2.imshow('Result', img)
cv2.waitKey(0)