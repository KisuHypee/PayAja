from qreader import QReader
from time import sleep


qreader = QReader()

def qr(img):
    data = qreader.detect_and_decode(image=img)
    if data:
        sleep(1)
        data = qreader.detect_and_decode(image=img)
        print("QR detected: ")
        for i in data:
            print (i)
        
        return True
    else:
        return False