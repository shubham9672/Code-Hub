def pan_checker():
    n = input("Enter PAN number:")
    n.upper()
    if n[:5].isalpha() and n[5:9].isdigit() and n[9:].isalpha():
        print("It's a VALID PAN")
    else:
        print("Invalid PAN")


if __name__ == "__main__":
    pan_checker()
