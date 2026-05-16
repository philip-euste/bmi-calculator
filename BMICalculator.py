from colorama import Fore

print("Welcome to the BMI calculator!")
weight_given = False
weight_choice_given = False
height_given = False
height_choice_given = False

while weight_given is False:
    try:
        weight = float(input("What is your weight(number)\n> "))
        break
    except ValueError:
        print(f"{Fore.LIGHTRED_EX}Input needs to be a real number, try again{Fore.RESET}")

def weight_result_func(multiplied=1.0, divided=1.0):
    print(f"You are {(weight * multiplied/divided):.2f} kg.")
    return weight * multiplied/divided

while weight_choice_given is False:
    weight_choice = input("What metric measure?(grams[g], pound[p], kilogram[k]\n> ").lower()
    if weight_choice == "p":
        weight_result = weight_result_func(divided=2.205)
        break
    elif weight_choice == "k":
        weight_result = weight_result_func()
        break
    elif weight_choice == "g":
        weight_result = weight_result_func(multiplied=0.001)
        break
    else:
        print(f"{Fore.LIGHTRED_EX}Please input a proper letter{Fore.RESET}")

while height_given is False:
    try:
        height = float(input("What is your height(number)\n> "))
        if height > 0:
            break
        else:
            print(f"{Fore.LIGHTRED_EX}Height can not be less than or equal to 0.{Fore.RESET}")
    except ValueError:
        print(f"{Fore.LIGHTRED_EX}Input an integer\nIt needs to be a whole number, try again{Fore.RESET}")


def height_result_func(divided=1.0):
    print(f"You are {height/divided:.2f} m.")
    return height/divided

while height_choice_given is False:
    height_choice = input("What metric measure?(inch[i], foot[f], meter[m], centimeter[cm]\n> ").lower()
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
        print(f"{Fore.LIGHTRED_EX}Please input a proper letter{Fore.RESET}")

BMI = weight_result/(height_result*height_result)

if BMI < 18.5:
    phrase = f"{Fore.LIGHTYELLOW_EX}underweight"
elif 25 > BMI >= 18.5:
    phrase = f"{Fore.LIGHTGREEN_EX}normal"
elif 30 > BMI >= 25:
    phrase = f"{Fore.LIGHTYELLOW_EX}overweight"
else:
     phrase = f"{Fore.LIGHTRED_EX}obese"

print(f"With a BMI of {BMI:.2f}. You are {phrase}{Fore.RESET} based on WHO guidelines.")
