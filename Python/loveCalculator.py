# Fun game to check the love percentage between a couple.

name1 = input("Enter the name of the 1st person: ")
name2 = input("Enter the name of the 2nd person: ")

name1 = name1.upper()
name2 = name2.upper()

love = 0

love += name1.count("T") + name2.count("T")
love += name1.count("R") + name2.count("R")
love += name1.count("U") + name2.count("U")
love += name1.count("E") + name2.count("E")

love *= 10

love += name1.count("L") + name2.count("L")
love += name1.count("O") + name2.count("O")
love += name1.count("V") + name2.count("V")
love += name1.count("E") + name2.count("E")

if love < 10 or love > 90:
    print(f"Your love score is {love}%, you go together like coke and mentos.")
elif love >=40 and love <=50:
    print(f"Your love score is {love}%, you are alright together.")
else:
    print(f"Your love score is {love}%.")