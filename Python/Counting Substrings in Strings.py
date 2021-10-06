#!/usr/bin/env python
# coding: utf-8

# In[ ]:


def count_substring(string, sub_string):                   #Creating a function named Count_String ,which takes the input of string and substring
    p=len(sub_string)                                      #Storig the length of string in a variable called p
    count=0                                                #Counter setting to zero
    for i in range(len(string)):                           #For loop for itterating through list
        if string[i:p+i]==sub_string:                      #Condition
            count=count+1                                  #If condition meet then incrementing the counter
    return count                                           #Returning count

if __name__ == '__main__':   
    string = input().strip()                               #Taking input 
    sub_string = input().strip()                           #Taking input sub_string
    count = count_substring(string, sub_string)            #Calling the function
    print(count)                                           #Printing Count

