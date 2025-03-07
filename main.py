import pytesseract
import numpy as np
import cv2 # OpenCV

#Download https://github.com/UB-Mannheim/tesseract/wiki
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

img = cv2.imread('src/Imagens/Aula1-teste.png')

# cv2.imshow('Imagem', img)
# cv2.waitKey(0)
# cv2.destroyAllWindows()

print(pytesseract.__version__)

texto = pytesseract.image_to_string(img)
print(texto)