#!/usr/bin/env python3


def main():
    num = int(input("Enter your desired Size of Palindromic Triangle : "))

    for i in range(1, num+1):
        print()
        for j in range(1, i+1):
            print(j, end=' ')
        for k in range(i, 1, -1):
            print(k-1, end= ' ')

main()