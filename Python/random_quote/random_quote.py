import random
import json

f = open('quotes.json',encoding="utf8")
 
data = json.load(f)

while True:
        
    print("============================\n\n")
    print("Choose one from options:\n")
    print(f"1- Type '1' to pick one quote from %d to %d \n"% (0,len(data)))
    print("2- Type '2' choose quote randomly\n")
    print("3- Type '3' to exit\n")
    print("============================\n\n")

    choice = input()

    if choice == "1":
        print(f"enter a value between %d and %d"% (0,len(data)))
        quote_index = int(input())
        if quote_index < len(data) and quote_index >= 0:
            print("##################\n")
            print(data[quote_index]["quote"])
            print(data[quote_index]["author"])
            print("\n##################")
        else:
            print(f"please! enter a value between %d and %d"% (0,len(data)))
    elif choice == "2":
        random_quote = random.choice(data)
        print(random_quote["quote"])
        print(f"Author: %s"% (random_quote["author"]))
    elif choice == "3":
        break
    else:
        print("enter a valid number 1 or 2")