import os

from PIL import Image

import pytesseract

def ocr(file_to_ocr):
    im = Image.open(file_to_ocr)
    txt=pytesseract.image_to_string(im)
    return txt

directory = os.path.join("/home/edo/tesi/articles")

#for i in range (1,17):
#    print(pytesseract.image_to_string("a1p"+str(i)+".jpg"))


with open("a1.txt", "w") as f:
    text=""

    for root,dirs,files in os.walk(directory):

        for file in files:
            if file.endswith(".jpg"):
                pre_fix=file[:-4]
                txt=ocr(file)
                text=text+txt

    f.write(text)
    f.close()
                


