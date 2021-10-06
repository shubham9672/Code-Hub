# -*- coding: utf-8 -*-
"""
Created on Mon Oct 12 08:44:39 2020

@author: innov
"""
yr = int(input("Enter any year:"))
if yr % 4 == 0:
    if yr %100 == 0:
        if yr % 400 == 0:
            print(yr,'is a leap year')
        else:
            print(yr,'is not a leap year')
    else:
        print(yr,'is a leap year')
else:
    print(yr,'is not a leap year')
