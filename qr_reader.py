from qreader import QReader
from cv2 import imread


qreader = QReader()

def qr(image):
    img = imread(image)
    print(f"The QR code goes to :{qreader.detect_and_decode(image=img)}")