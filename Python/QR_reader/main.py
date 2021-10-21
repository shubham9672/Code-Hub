
import cv2
from pyzbar import pyzbar


def read_code(frame):
    codes = pyzbar.decode(frame)
    for code in codes:
        x, y, w, h = code.rect
        code_info = code.data.decode('utf-8')
        cv2.rectangle(frame, (x, y), (x + w, y + h), (0, 255, 0), 2)

        font = cv2.FONT_HERSHEY_DUPLEX
        cv2.putText(frame, code_info, (x + 6, y - 6), font, 2.0, (255, 255, 255), 1)
        with open("qr_code_result.txt", mode='w') as file:
            file.write("Recognized code:" + code_info)
    return frame


def readQR():
    camera = cv2.VideoCapture(0)
    ret, frame = camera.read()
    while ret:
        ret, frame = camera.read()
        frame = read_code(frame)
        cv2.imshow('QR code reader', frame)
        if cv2.waitKey(1) & 0xFF == 27:
            break
    camera.release()
    cv2.destroyAllWindows()


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    readQR()

