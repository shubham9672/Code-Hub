# Manish Bishowkarma
# 14 Oct, 2021
# From Score to letter Grade

print("\n\t\t\tGrade Determine Program!!!\n")


def determine_grade():
    choice = "y"
    while choice != "n":
        try:
            score = int(input("Please enter score(0 - 100): "))

        except:
            print("Please enter the numeric value!!!")
            quit()

        if 0 > score > 100:
            print("Please enter the value between 0 to 100!!!")
        elif score >= 90:
            print("Your grade is A")
        elif score >= 80:
            print("Your grade is B")
        elif score >= 70:
            print("Your grade is C")
        elif score >= 60:
            print("Your grade is D")
        else:
            print("Your grade is F")

        choice = input("\ndo you want to enter again(y/n)?: ")
        if choice == "n":
            print("Thank you.Good-Bye")
            break


determine_grade()
