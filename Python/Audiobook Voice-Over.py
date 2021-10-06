#Importing the libraries
import cv2
import pytesseract
from PIL import Image
from gtts import gTTS
from playsound import playsound
# Specifying the path
pytesseract.pytesseract.tesseract_cmd = r'C:/Program Files/Tesseract-OCR/tesseract.exe'

# Reading the image 
image = cv2.imread('1.png')

# Extraction of text from image
text = pytesseract.image_to_string(image)

# Printing the text
print(text)
# Create the voice_text variable to store the data.

voice_text = ""

# Pre-processing the data

for i in text.split():
    voice_text += i + ' '
    
voice_text = voice_text[:-1]
voice_text

tts = gTTS(voice_text)
tts.save("test.mp3")
playsound("test.mp3")