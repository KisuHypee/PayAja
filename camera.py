import cv2
import qr_reader

def QRscanner():
    cam = cv2.VideoCapture(0)
    reading_qr = False

    # Get the default frame width and height
    frame_width = int(cam.get(cv2.CAP_PROP_FRAME_WIDTH))
    frame_height = int(cam.get(cv2.CAP_PROP_FRAME_HEIGHT))

    while True:
        ret, frame = cam.read()

        # Display the captured frame
        cv2.imshow('Camera', frame)
        decryption = qr_reader.qr(frame)
        if decryption:
            break

        # Press 'q' to exit the loop, just in case button
        if cv2.waitKey(1) == ord('q'):
            break

    # Release the capture and writer objects
    cam.release()
    cv2.destroyWindow('Camera')
    return decryption
