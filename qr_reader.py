from qreader import QReader
from webbrowser import open


qreader = QReader() #Used for the QR detection fuction


def qr(img):
    data = qreader.detect_and_decode(image=img) #Scans the QR code
    if data: #if QR code was detected
        for i in data:

            if i == None: #Occurs when scanned code is invalid
                print("Please bring the QR closer to the camera")
                break #Code continues running

            return i
    return False