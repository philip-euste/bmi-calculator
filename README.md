# 🧮 BMI Calculator

A simple Python BMI (Body Mass Index) calculator with:

* ✅ Multiple unit support
* 🎨 Colored terminal output using Colorama
* ⚠️ Input validation
* 🌍 WHO BMI classification guidelines
---

## Version

****v3.0.0****

---

## ✨ Features

* Supports different weight units:

  * Grams (`g`)
  * Pounds (`p`)
  * Kilograms (`k`)

* Supports different height units:

  * Inches (`i`)
  * Feet (`f`)
  * Meters (`m`)
  * Centimeters (`cm`)

* Automatically converts everything into:

  * kilograms (kg)
  * meters (m)

* Displays BMI category with colored text:

  * 🟡 Underweight
  * 🟢 Normal
  * 🟡 Overweight
  * 🔴 Obese

---

## 📦 Requirements

Install dependencies before running:

```bash
pip install colorama
```

---

## ▶️ Running the Program

```bash
python bmi_calculator.py
```

---

## 🖥️ Example

```text
Welcome to the BMI calculator!

What is your weight(number)
> 150

What metric measure?(grams[g], pound[p], kilogram[k]
> p

You are 68.03 kg.

What is your height(number)
> 175

What metric measure?(inch[i], foot[f], meter[m], centimeter[cm]
> cm

You are 1.75 m.

With a BMI of 22.21. You are normal based on WHO guidelines.
```

---

## 📚 BMI Categories Used

Based on simplified WHO guidelines:

| BMI         | Category    |
| ----------- | ----------- |
| Below 18.5  | Underweight |
| 18.5 - 24.9 | Normal      |
| 25 - 29.9   | Overweight  |
| 30+         | Obese       |

> ⚠️ This is only a rough estimate and does not account for age, muscle mass, or medical conditions.

---

## 🛠️ Built With

* 🐍 Python
* 🎨 Colorama

---

## 🚧 Future Ideas

* [ ] Add GUI version
* [ ] Add age support
* [ ] Add imperial BMI output
* [ ] Save BMI history
* [ ] Health recommendations

---

## 📄 License

Free to use and modify for learning purposes.