import pytesseract

pytesseract.pytesseract.tesseract_cmd = r"C:\Program Files\Tesseract-OCR\tesseract.exe"
langueges = pytesseract.get_languages(config='')


print(langueges)