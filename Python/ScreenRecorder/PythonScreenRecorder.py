from PIL import ImageGrab
import numpy as np
import cv2
import datetime
import keyboard

image = ImageGrab.grab()
width, height = image.size
print("width:", width, "height:", height)
print("image mode:", image.mode)


time1 = datetime.datetime.now().strftime("%Y-%m-%d %H-%M")
test = f"{time1}.mp4"
fourcc = cv2.VideoWriter_fourcc(*"mp4v")  # format of the file 
capture_video = cv2.VideoWriter(test, fourcc, 9.5, (width, height))
print("video recording !!!!!")


while True:
    rgb = ImageGrab.grab(bbox=(0, 0, width, height))
    img_rgb = np.array(rgb)
    img_bgr = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2RGB)
    capture_video.write(img_bgr)
    if keyboard.is_pressed("^"): #KEY TO PRESS TO FINISH SCREEN RECORDING
        break


print("\nScreen Recording Done!!")
cv2.destroyAllWindows()
capture_video.release()
