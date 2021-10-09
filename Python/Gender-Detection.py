

import cv2
import cvlib as cv
import sys
import numpy as np
from numpy.lib.type_check import image
image = cv2.imread("MY.png")


face, confidence = cv.detect_face(image)
padding = 20

for i in face:
    (x, y) = max(0, i[0]-padding), max(0, i[1]-padding)
    (x2, y2) = min(image.shape[1]-1, i[2]+padding), min(image.shape[0]-1,i[3]+padding)
    cv2.rectangle(image, (x, y), (x2, y2), (0, 255, 0), 2)
    crop = np.copy(image[y:y2, x:x2])
    (label, confidence) = cv.detect_gender(crop)
    idx = np.argmax(confidence)
    label = label[idx]
    label = "{}: {:.2f}%".format(label, confidence[idx] * 100)
    Y = y - 10 if y -10 > 10 else y + 10
    cv2.putText(image, label, (y, Y), cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)

cv2.imshow("Gender Detection", image)
cv2.waitKey()
cv2.destroyAllWindows()