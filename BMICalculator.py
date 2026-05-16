print("Welcome to the BMI calculator!")
weight_given = False
weight_choice_given = False
height_given = False
height_choice_given = False
weight = 0
height = 0

while weight_given is False:
    try:
        weight = float(input("What is your weight(number)\n> "))
        break
    except ValueError:
        print("You are lying, input a real number\nIt needs to be a number, try again")

def weight_result_func(multiplied=1.0):
    print("You are " + str(weight * multiplied) + " kg.")
    return weight * multiplied

while weight_choice_given is False:
    weight_choice = input("What metric measure?(grams[g], pound[p], kilogram[k]\n> ")
    if weight_choice == "p":
        weight_result = weight_result_func(2.205)
        break
    elif weight_choice == "k":
        weight_result = weight_result_func()
        break
    elif weight_choice == "g":
        weight_result = weight_result_func(0.001)
        break
    else:
        print("Please input a proper letter")

while height_given is False:
    try:
        height = float(input("What is your height(number)\n> "))
        if int(height) != 0:
            break
        else:
            print("Height can not be 0")
    except ValueError:
        print("Input an integer\nIt needs to be a whole number, try again")


def height_result_func(divided=1.0):
    print("You are " + str(height/divided) + " m.")
    return height/divided

while height_choice_given is False:
    height_choice = input("What metric measure?(inch[i], foot[f], meter[m], centimeter[cm]\n> ")
    if height_choice == "i":
        height_result = height_result_func(39.37)
        break
    elif height_choice == "m":
        height_result = height_result_func()
        break
    elif height_choice == "f":
        height_result = height_result_func(3.281)
        break
    elif height_choice == "cm":
        height_result = height_result_func(100)
        break
    else:
        print("Please input a proper letter")

BMI = weight_result/(height_result*height_result)

print("Your BMI is " + str(BMI) + ".")
if BMI < 18.5:
    print("You are underweight")
elif 24.9 > BMI >= 18.5:
    print("You are at risk of being underweight")
elif 29.9 > BMI > 25:
    print("You are normal")
elif 34.9 > BMI > 30:
    print("You are overweight")
elif BMI > 35:
    print("You are obese")