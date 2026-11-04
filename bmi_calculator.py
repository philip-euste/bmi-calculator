from helper_functions import weight_height_func, weight_string_func, height_string_func, bmi_result_func

def main():
    print("Welcome to the BMI calculator!")

    weight_result: float = weight_string_func(weight_height_func("weight"))
    height_result: float = height_string_func(weight_height_func("height"))
    print(bmi_result_func(weight_result, height_result))

if __name__ == "__main__":
    main()