def caesar_encrypt(word, n):
    c = ""
    for i in word:
        if not i.isalpha():
            c += i
        elif i.isupper():
            c += chr((ord(i) + n - 65) % 26 + 65)
        else:
            c += chr((ord(i) + n - 97) % 26 + 97)
    return c


def caesar_decrypt(word, n):
    c = ""
    for i in word:
        if not i.isalpha():
            c += i
        elif i.isupper():
            c += chr((ord(i) - n - 65) % 26 + 65)

        # Encrypt lowercase characters
        else:
            c += chr((ord(i) - n - 97) % 26 + 97)
    return c


plain = input()
n = int(input())
cipher = caesar_encrypt(plain, n)
print(cipher)
decipher = caesar_decrypt(cipher, n)
print(decipher)
