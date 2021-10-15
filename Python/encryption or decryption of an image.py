from tkinter import * #using this library to create the GUI
from tkinter import filedialog #it will help us open the file selection option

#now firstly we'll build the GUI

root = Tk() # instance
root.geometry("200x160")

# function (which will extract the image and then ecrypt it)
def encrypt_image():
    # file dialog box
    # file1 = variable with one method (which will ask to open the file)
    # method will accept 2 parameters mode(read(extract), write(put)) and the type of the file
    file1 = filedialog.askopenfile(mode='r', filetype = [('jpg file','*.jpg'),('png file','*.png')])

    # now we'll check that our file variable is empty or not
    if file1 is not None:
        print(file1)

        # file name = variable
        # print the file name
        file_name = file1.name
        print(file_name)

        # key variable to get the exact file name from start to end
        key = entry1.get(1.0, END)
        print(file_name, key)

        #now we need to extract the data from the specific file
        #we created the fi variable and then we'll open the file name which has the path
        #the file name of the selected image and we have used the rb method which will read the data in the byte format
        fi = open(file_name, 'rb')
        image = fi.read() # read the file
        fi.close() #close the file

        #now we need to convert the data into byte array so that we can perform the operations
        #because initially data is present in the pixel intensities we are converting it into byte values
        image = bytearray(image)

        #now the enumerate method will provide the index/address to all the values
        for index, values in enumerate(image):

#as the A tuple is a collection which is ordered and unchangeable. so we can't provide index there but we can provide
#that on lists and strings (basically used for iterable varibales like while loop, arrays function

# we'll edit the values so for image of index we want to change the values
#we'll use the XOR operator to get the interchangeable values
            image[index] = values^int(key)#values are changed
             #lets save the values in the file back
        fi1 = open(file_name, 'wb') #wb method because we are going to write the data
        fi1.write(image)
        fi1.close()

#button which will open that file dialog box
#all the value of button will be saved in b1 variable (button is the method name so B should be capital)
# root = GUI instance
# text = which will be present on our button, which is encrypt
# command = the action which button will trigger a function called encrypt_image
b1 = Button(root, text = "ENCRYPT/DECRYPT" , command = encrypt_image)

# lets assume the screen is in the form of coordinates and the placement of our button is on x and y axis
b1.place(x = 40, y = 10)

#entry widget which will ask the user for the key
# entry1 = variable
# text = method name (root = GUI instance, height pof our text box, width of our text box)
entry1 = Text(root, height = 1, width = 15)

#we have placed our entry widget exact in the center position
entry1.place(x = 40, y = 50)

root.mainloop()

