import cv2
from pytesseract import pytesseract


# ler a imagem
imagem = cv2.imread(r"C:\Users\Win10\Pictures\imagem de programas\csv bites\i2.jpeg")

# tesseract extrair o texto
path_to_tesseract = r"C:\Program Files\Tesseract-OCR"

pytesseract.tesseract_cmd = path_to_tesseract + r"\tesseract.exe"

texto = pytesseract.image_to_string(imagem)

print(texto)