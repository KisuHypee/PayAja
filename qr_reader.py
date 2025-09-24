from qreader import QReader


qreader = QReader()



def qr(img):
    data = qreader.detect_and_decode(image=img)
    if data:
        data = qreader.detect_and_decode(image=img)
        for i in data:
            if i == None:
                print("Please bring the QR closer to the camera")
                break
            print (i)
            return True



 
    return False