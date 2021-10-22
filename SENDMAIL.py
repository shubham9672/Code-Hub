import smtplib as s

ob = s.SMTP("smtp.gmail.com",587)
ob.starttls()
ob.login(user='youremail',password='password')

subject ="Sending Email using Python"

body = "Testing Sending email using python script"

message = "Subject:{}\n\n{}".format(subject,body)
print(message)
listOfAddress =['receiveremail1@mail.com','receiveremail2@mail.com','receiveremail3@mail.com']
ob.sendmail("senderemail@mail.com",listOfAddress,message)
print("Email sended successfully")
ob.quit()