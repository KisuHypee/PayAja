from qreader import QReader
from time import process_time


qreader = QReader()
reading = False


def qr(img):
    global reading
    data = qreader.detect_and_decode(image=img)
    if data:
        if reading:
            end_count = process_time()
            time_diff = end_count - start_count
            if time_diff >= 5:
                data = qreader.detect_and_decode(image=img)
                print("QR detected: ")
                for i in data:
                    print (i)
                
                return True
        else:
            start_count = process_time()
            reading = True

 
    return False