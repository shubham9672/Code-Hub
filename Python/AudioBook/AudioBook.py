import pyttsx3
import PyPDF2

print("WELCOME TO AUDIOBOOK")
filename = input("Enter name of input file(with .pdf extension):")
book = open(filename, "rb")
pdfReader = PyPDF2.PdfFileReader(book)
pages = pdfReader.numPages
print("The number of pages of the pdf are: " + str(pages))  # prints number of pages

speaker = pyttsx3.init()  # Initialize the speaker

"""Adding Rate Controls"""
rate = speaker.getProperty("rate")
user_rate = int(
    input("At what rate do you want to hear Audiobook?")
)  # taking reading rate input from user
speaker.setProperty("rate", user_rate)
# rate=170 is normal speed, you can increase and decrease as per your convenience

"""Adding VOLUME Controls"""
volume = int(input("Please Enter the desired volume (0-100) "))
speaker.setProperty("volume", 0.01 * volume)  # setting up volume level  between 0 and 1

"""Adding VOICE Controls"""
voices = speaker.getProperty("voices")  # getting details of current voice

input_voice = int(input("Enter 1 for Male voice and 2 for female voice "))

if input_voice == 1:
    speaker.setProperty(
        "voice", voices[0].id
    )  # changing index, changes voices. o for male
else:
    speaker.setProperty(
        "voice", voices[1].id
    )  # changing index, changes voices. 1 for female


"""Reading the pdf"""
user_input = int(input("Enter the starting page:"))
for i in range(user_input, pages):
    page = pdfReader.getPage(i)
    text = page.extractText()
    speaker.say(text)
    speaker.runAndWait()
speaker.stop()
print("Thank you")
