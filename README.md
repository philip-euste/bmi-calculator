# BMI Calculator

A Python-based Body Mass Index (BMI) calculator that supports multiple measurement units, validates user input, converts measurements into standardized units, and classifies BMI results using the **WHO adult BMI classification**.

---

## Version

**v3.0.0**

---

## Features

- Support multiple weight measurement units:
  - Grams (`g`)
  - Pounds (`p`)
  - Kilograms (`k`)
- Support multiple height measurement units:
  - Inches (`i`)
  - Feet (`f`)
  - Meters (`m`)
  - Centimeters (`cm`)
- Automatically convert measurements into standardized units:
  - Weight → Kilograms (kg)
  - Height → Meters (m)
- Validate numerical inputs and measurement units.
- Reject zero and negative measurements.
- Handle invalid inputs through repeated prompts.
- Calculate Body Mass Index (BMI).
- Classify BMI results using WHO adult BMI categories.
- Display measurement conversions and BMI results to two decimal places.
- Apply colored terminal output using Colorama.
- Separate the program into modular Python files for better code organization.

---

## Project Structure

```text
bmi-calculator/
├── bmi_calculator.py
├── helper_functions.py
├── colors.py
├── requirements.txt
├── README.md
└── LICENSE
```

---

## Explanation

The program processes user input through four main stages:

1. **Input Collection** — Request the user's weight and height, including their respective measurement units.
2. **Conversion** — Convert the collected measurements into kilograms and meters.
3. **Calculation** — Calculate BMI using the standardized measurements.
4. **Classification** — Determine the corresponding WHO adult BMI category and display the result.

The complete pipeline is:

```text
User Input
    ↓
Input Validation
    ↓
Unit Conversion
    ↓
BMI Calculation
    ↓
BMI Classification
    ↓
Terminal Output
```

### Input Collection and Validation

The program requests numerical weight and height values through `weight_height_func()`.

Input validation ensures that:

- Inputs must be valid numerical values.
- Inputs must be greater than zero.
- Invalid numerical inputs trigger an error message.
- Invalid measurements are requested again.

The program uses exception handling through `try` and `except ValueError` to handle invalid numerical inputs.

### Weight Conversion

The weight conversion stage accepts three measurement units and converts them into kilograms.

| Unit | Conversion |
|---|---|
| Grams (g) | Weight × 0.001 |
| Pounds (p) | Weight ÷ 2.205 |
| Kilograms (k) | Weight × 1 |

The conversion is handled by `weight_string_func()` and `weight_result_func()`.

### Height Conversion

The height conversion stage accepts four measurement units and converts them into meters.

| Unit | Conversion |
|---|---|
| Inches (i) | Height ÷ 39.37 |
| Feet (f) | Height ÷ 3.281 |
| Meters (m) | Height ÷ 1 |
| Centimeters (cm) | Height ÷ 100 |

The conversion is handled by `height_string_func()` and `height_result_func()`.

### BMI Calculation

The program calculates BMI using the standard formula:

\[
BMI = \frac{Weight\ (kg)}{Height\ (m)^2}
\]

The calculation is implemented in `bmi_result_func()`.

### BMI Classification

The resulting BMI is classified using simplified WHO adult BMI classification thresholds.

| BMI | Category |
|---|---|
| Below 18.5 | Underweight |
| 18.5–24.9 | Normal |
| 25.0–29.9 | Overweight |
| 30.0 and above | Obese |

Each category is displayed using a corresponding terminal color:

- Yellow — Underweight
- Green — Normal
- Yellow — Overweight
- Red — Obese

These thresholds are intended for adults and should not be used to interpret BMI in children or teenagers. BMI is also a screening measure rather than a complete assessment of health.

### Terminal Colors

The project uses Colorama to provide colored terminal output.

Color definitions are centralized in `colors.py`:

| Variable | Color |
|---|---|
| `FF` | Reset |
| `FLR` | Light Red |
| `FLY` | Light Yellow |
| `FLG` | Light Green |

The `invalid_print()` function in `helper_functions.py` also centralizes error message formatting.

### Modular Organization

The project separates its responsibilities into three Python files:

- **`bmi_calculator.py`** — Contains the main program entry point and coordinates the calculation pipeline.
- **`helper_functions.py`** — Contains input validation, unit conversion, BMI calculation, and classification functions.
- **`colors.py`** — Contains centralized Colorama color definitions.

---

## Installation

Clone the repository:

```bash
git clone https://github.com/yourusername/bmi-calculator.git

cd bmi-calculator
```

### Requirements

Install the required dependency:

```bash
pip install colorama
```

Alternatively, install dependencies using `requirements.txt`:

```bash
pip install -r requirements.txt
```

---

## Usage

Run the program:

```bash
python bmi_calculator.py
```

The program will:

1. Request the user's weight.
2. Request the corresponding weight measurement unit.
3. Convert the weight into kilograms.
4. Request the user's height.
5. Request the corresponding height measurement unit.
6. Convert the height into meters.
7. Calculate BMI.
8. Display the BMI classification.

---

## Example

```text
Welcome to the BMI calculator!

What is your weight(number)
> 150

What metric measure?(grams[g], pound[p], kilogram[k])
> p

You are 68.03 kg.

What is your height(number)
> 175

What metric measure?(inch[i], foot[f], meter[m], centimeter[cm])
> cm

You are 1.75 m.

With a BMI of 22.21, you are classified as normal
based on the WHO adult BMI classification.
```

---

## Dependencies

**Python 3.10+**

External dependencies:

- `colorama`

Standard Library:

- `typing` (type annotations)
- `builtins` (input/output)
- `ValueError` (input validation)

---

## Future Improvements

- [ ] Add a graphical user interface (GUI).
- [ ] Add age-appropriate BMI interpretation.
- [ ] Add BMI history tracking.
- [ ] Add support for additional measurement units.
- [ ] Improve input validation and error handling.
- [ ] Add automated unit tests.
- [ ] Improve terminal output formatting.

---

## Attribution

This project is an independent Python programming project developed for educational and learning purposes.

BMI classification thresholds are based on the World Health Organization's adult BMI classification.

## License

This project is licensed under the **MIT License**. See the `LICENSE` file for details.