# This script is created by Arijit Paul / Text to Hand Writing
#  GitHub : https://github.com/Darkethic06/
import pywhatkit as pwt

fo =open("<loaction of the text file>", "r",  encoding="utf8",)

str = fo.read()

# store the png file 
pwt.text_to_handwriting(str,"<location of the file>",rgb=[0,0,255])
