def palindrome(vlaue):
    return vlaue.lower() == vlaue[::-1].lower()

print(palindrome("Racecar"))
