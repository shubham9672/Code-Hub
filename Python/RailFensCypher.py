def encryptRailFence(text, key):
    rail = [["\n" for i in range(len(text))] for j in range(key)]
    dir_down = False
    row, col = 0, 0

    for i in range(len(text)):
        if (row == 0) or (row == key - 1):
            dir_down = not dir_down

        rail[row][col] = text[i]
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    result = []
    for i in range(key):
        for j in range(len(text)):
            if rail[i][j] != "\n":
                result.append(rail[i][j])
    return "".join(result)


def decryptRailFence(cipher, key):
    rail = [["\n" for i in range(len(cipher))] for j in range(key)]
    dir_down = None
    row, col = 0, 0
    for i in range(len(cipher)):
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False
        rail[row][col] = "*"
        col += 1
        if dir_down:
            row += 1
        else:
            row -= 1
    index = 0
    for i in range(key):
        for j in range(len(cipher)):
            if (rail[i][j] == "*") and (index < len(cipher)):
                rail[i][j] = cipher[index]
                index += 1
    result = []
    row, col = 0, 0
    for i in range(len(cipher)):

        # check the direction of flow
        if row == 0:
            dir_down = True
        if row == key - 1:
            dir_down = False

        if rail[row][col] != "*":
            result.append(rail[row][col])
            col += 1

        if dir_down:
            row += 1
        else:
            row -= 1
    return "".join(result)


if __name__ == "__main__":
    s = input("Enter the text:")
    n = int(input("Key:"))
    str = encryptRailFence(s, n)
    print(f"Encrypted Text:{str}")
    print(f"Decrypted Text:{decryptRailFence(str, n)}")
