from colors import FLR, FLY, FLG, FF

def invalid_print(string: str, error_color: str = FLR) -> None:
    print(f"{error_color}{string}{FF}")

# ! WEIGHT HEIGHT FUNCTIONS

def weight_height_func(type: str) -> float:
    while True:
        try:
            weight_height = float(input(f"\nWhat is your {type}(number)\n> "))
            if weight_height <= 0:
                invalid_print(f"{type.title()} can not be less than or equal to 0.")
                continue
            return weight_height
        except ValueError:
            invalid_print("Input needs to be a real number, try again")

# ! WEIGHT FUNCTIONS

def weight_string_func(weight: float) -> float:
    while True:
        weight_choice = input("\nWhat metric measure?(grams[g], pound[p], kilogram[k]\n> ").strip().lower()
        if weight_choice == "p":
            weight_result = weight_result_func(weight, divided = 2.205)
        elif weight_choice == "k":
            weight_result = weight_result_func(weight)
        elif weight_choice == "g":
            weight_result = weight_result_func(weight, multiplied = 0.001)
        else:
            invalid_print("Please input a proper letter")
            continue
        return weight_result

def weight_result_func(weight: float, multiplied: float = 1.0, divided: float = 1.0) -> float:
    print(f"You are {(weight * multiplied / divided):.2f} kg.")
    return weight * multiplied/divided

# ! HEIGHT FUNCTIONS

def height_string_func(height: float) -> float:
    while True:
        height_choice = input("\nWhat metric measure?(inch[i], foot[f], meter[m], centimeter[cm]\n> ").strip().lower()
        if height_choice == "i":
            height_result = height_result_func(height, 39.37)
        elif height_choice == "m":
            height_result = height_result_func(height)
        elif height_choice == "f":
            height_result = height_result_func(height, 3.281)
        elif height_choice == "cm":
            height_result = height_result_func(height, 100)
        else:
            invalid_print("Please input a proper letter")
            continue
        return height_result

def height_result_func(height: float, divided = 1.0):
    print(f"You are {height / divided:.2f} m.")
    return height / divided

# ! BMI FUNCTIONS

def bmi_result_func(weight: float, height: float) -> str:
    BMI = weight/(height**2)
    if BMI < 18.5:
        phrase = f"{FLY}underweight"
    elif 25 > BMI >= 18.5:
        phrase = f"{FLG}normal"
    elif 30 > BMI >= 25:
        phrase = f"{FLY}overweight"
    else:
        phrase = f"{FLR}obese"

    return f"\nWith a BMI of {BMI:.2f}, you are classified as {phrase}{FF} based on the WHO adult BMI classification"