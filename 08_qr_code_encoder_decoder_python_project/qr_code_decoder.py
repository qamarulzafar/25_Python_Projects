import cv2

def decode_qr(image_path):
    img = cv2.imread(image_path)
    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(img)


    if bbox is not None and data:
        print('Qr Code Data', data)
    else:
        print('No QR code found in the image.')


path = input("Enter the path to the QR code image: ")
decode_qr(path)