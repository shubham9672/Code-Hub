import pywhatkit
from datetime import datetime

now = datetime.now()

chour = now.strftime("%H")
mobile = input('Enter Mobile No of Receiver : ')  # Enter mobile number along with country code
message = input('Enter Message you wanna send : ') 
hour = int(input('Enter hour : '))       # Enter hour as per 24 hour format
minute = int(input('Enter minute : '))   # Enter value between 0-59

pywhatkit.sendwhatmsg(mobile,message,hour,minute)
