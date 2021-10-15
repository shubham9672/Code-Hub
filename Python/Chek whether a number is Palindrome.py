# Chek whether a number is Palindrome
def isPalindrome(num=int(input("Enter a number:"))):

    temp = num
    rev = 0
    while num > 0:
        dig = num % 10
        rev = rev * 10 + dig
        num = num // 10
    if temp == rev:
        print("The number is a palindrome!")
    else:
        print("The number isn't a palindrome!")


print(isPalindrome())
