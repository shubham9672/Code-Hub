# Provide your height and weight, we will calculate your bmi

H = input("Enter your height(in m): ")
W = input("Enter your weight(in kg): ")

h = float(H)
w = float(W)

bmi = w/h**2

if bmi < 16:
    print("\nYour BMI: " + str(round(bmi,2)))
    print("You are Underweight (Severe thinness)")
elif bmi >= 16 and bmi < 17:
    print("\nYour BMI: " + str(round(bmi,2)))
    print("You are Underweight (Moderate thinness)")
elif bmi >= 17 and bmi < 18.5:
    print("\nYour BMI: " + str(round(bmi,2)))
    print("You are Underweight (Mild thinness)")
elif bmi >= 18.5 and bmi < 25:
    print("\nYour BMI: " + str(round(bmi,2)))
    print("You are Normal")
elif bmi >= 25 and bmi < 30:
    print("\nYour BMI: " + str(round(bmi,2)))
    print("Overweight (Pre-Obese)")
elif bmi >= 30 and bmi < 35:
    print("\nYour BMI: " + str(round(bmi,2)))
    print("Obese (Class I)")
elif bmi >= 35 and bmi < 40:
    print("\nYour BMI: " + str(round(bmi,2)))
    print("Obese (Class II)")
else:
    print("\nYour BMI: " + str(round(bmi,2)))
    print("Obese (Class III)")