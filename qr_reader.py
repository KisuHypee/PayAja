from qreader import QReader
from cv2 import imread


qreader = QReader()

img = imread("qr-code.webp")

print(f"The QR code goes to :{qreader.detect_and_decode(image=img)}")