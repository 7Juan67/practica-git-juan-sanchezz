"""
Student Name: Juan Jassiel Sanchez Melendez
Student ID (Matricula): 2630209
Group: IM 1 - 2
GitHub Repository: https://github.com/7Juan67/practica-git-juan-sanchezz
"""

# EXECUTIVE SUMMARY / RESUMEN EJECUTIVO
"""
In Python, numeric data is mainly represented by two types: integers (int), which
store whole numbers without decimals, and floating-point numbers (float), which
store real numbers with decimal points for precise measurements. A boolean (bool)
is a logical data type that only has two values: True or False, and it is obtained
by evaluating comparisons with relational operators (<, >, <=, >=, ==, !=) or
combining conditions with logical operators (and, or, not). Validating numeric
ranges and preventing division by zero is critical to avoid execution crashes and
stop impossible data (such as negative work hours or zero height). This file covers
6 problems demonstrating input design, validations, type casting, arithmetic
calculations, and boolean flags tested with normal, border, and error cases.
"""

# PRINCIPLES AND BEST PRACTICES / PRINCIPIOS Y BUENAS PRACTICAS
"""
1. Use appropriate data types: int for whole counters and float for decimal values.
2. Avoid duplicating complex expressions by saving intermediate results in variables.
3. Always validate input data before calculating (avoid negative values or zero division).
4. Use clear lower_snake_case variable names, UPPER_SNAKE_CASE constants, and English messages.
5. Document clearly what each boolean flag represents (what True and False mean in context).
"""


# PROBLEM 1: TEMPERATURE CONVERTER AND RANGE FLAG
"""
Problem 1: Temperature converter and range flag
Description:
Converts a temperature in Celsius (float) to Fahrenheit and Kelvin, and sets a
boolean flag (is_high_temperature) to True if Celsius is 30.0 or higher, and
False otherwise.

Inputs:
- temp_c (float; temperature in Celsius)

Outputs:
- Fahrenheit: <temp_f>
- Kelvin: <temp_k>
- High temperature: true|false

Validations:
- Verify that temp_c can be converted to float.
- Do not allow physically impossible temperatures in Kelvin (temp_k < 0.0).

Test cases:
1) Normal: "25.0" -> Fahrenheit: 77.0, Kelvin: 298.15, High temperature: false
2) Border: "30.0" -> Fahrenheit: 86.0, Kelvin: 303.15, High temperature: true
3) Error: "-300.0" -> Error: invalid input (Kelvin is less than 0.0)
"""

print("--- PROBLEM 1: TEMPERATURE CONVERTER AND RANGE FLAG ---")

KELVIN_OFFSET = 273.15
ABSOLUTE_ZERO_K = 0.0
HIGH_TEMP_LIMIT_C = 30.0

p1_test_inputs = ["25.0", "30.0", "-300.0"]

for raw_temp in p1_test_inputs:
    clean_temp = raw_temp.strip()
    # Remove one minus sign and one decimal point to check if text is numeric
    temp_digits = clean_temp.replace("-", "", 1).replace(".", "", 1)

    if len(clean_temp) == 0 or not temp_digits.isdigit():
        print("Error: invalid input")
    else:
        temp_c = float(clean_temp)
        temp_f = temp_c * 9 / 5 + 32
        temp_k = temp_c + KELVIN_OFFSET

        if temp_k < ABSOLUTE_ZERO_K:
            print("Error: invalid input")
        else:
            # Boolean flag: True if temperature is 30.0 C or above
            is_high_temperature = bool(temp_c >= HIGH_TEMP_LIMIT_C)

            print(f"Fahrenheit: {round(temp_f, 2)}")
            print(f"Kelvin: {round(temp_k, 2)}")
            print(f"High temperature: {str(is_high_temperature).lower()}")


# PROBLEM 2: WORK HOURS AND OVERTIME PAYMENT
"""
Problem 2: Work hours and overtime payment
Description:
Calculates weekly pay for a worker. Up to 40 hours are paid at the regular
hourly_rate, while overtime hours (over 40) are paid at 150% of the normal rate.
Also generates a boolean flag (has_overtime) indicating if overtime was worked.

Inputs:
- hours_worked (float; hours worked in the week)
- hourly_rate (float; payment per hour)

Outputs:
- Regular pay: <regular_pay>
- Overtime pay: <overtime_pay>
- Total pay: <total_pay>
- Has overtime: true|false

Validations:
- hours_worked >= 0.0
- hourly_rate > 0.0

Test cases:
1) Normal: hours_worked = 45.0, hourly_rate = 100.0 -> Regular: 4000.0, Overtime: 750.0, Total: 4750.0, Has overtime: true
2) Border: hours_worked = 40.0, hourly_rate = 100.0 -> Regular: 4000.0, Overtime: 0.0, Total: 4000.0, Has overtime: false
3) Error: hours_worked = -5.0, hourly_rate = 100.0 -> Error: invalid input
"""

print("\n--- PROBLEM 2: WORK HOURS AND OVERTIME PAYMENT ---")

MAX_REGULAR_HOURS = 40.0
OVERTIME_RATE_FACTOR = 1.5
MIN_VALID_HOURS = 0.0
MIN_VALID_RATE = 0.0

p2_hours = [45.0, 40.0, -5.0]
p2_rates = [100.0, 100.0, 100.0]

for index in [0, 1, 2]:
    hours_worked = float(p2_hours[index])
    hourly_rate = float(p2_rates[index])

    if hours_worked < MIN_VALID_HOURS or hourly_rate <= MIN_VALID_RATE:
        print("Error: invalid input")
    else:
        regular_hours = min(hours_worked, MAX_REGULAR_HOURS)
        overtime_hours = max(0.0, hours_worked - MAX_REGULAR_HOURS)

        regular_pay = regular_hours * hourly_rate
        overtime_pay = overtime_hours * hourly_rate * OVERTIME_RATE_FACTOR
        total_pay = regular_pay + overtime_pay

        # Boolean flag: True only when hours_worked exceeds 40.0
        has_overtime = bool(hours_worked > MAX_REGULAR_HOURS)

        print(f"Regular pay: {round(regular_pay, 2)}")
        print(f"Overtime pay: {round(overtime_pay, 2)}")
        print(f"Total pay: {round(total_pay, 2)}")
        print(f"Has overtime: {str(has_overtime).lower()}")


# PROBLEM 3: DISCOUNT ELIGIBILITY WITH BOOLEANS
"""
Problem 3: Discount eligibility with booleans
Description:
Determines if a customer qualifies for a 10% discount. The customer is eligible
if is_student is True, OR is_senior is True, OR purchase_total is at least 1000.0.
Calculates and displays the final total to pay.

Inputs:
- purchase_total (float; total amount of purchase)
- is_student_text (string; "YES" or "NO")
- is_senior_text (string; "YES" or "NO")

Outputs:
- Discount eligible: true|false
- Final total: <final_total>

Validations:
- purchase_total >= 0.0
- Normalize is_student_text and is_senior_text to uppercase and validate that
  both are strictly "YES" or "NO".

Test cases:
1) Normal: 500.0, "yes", "no" -> Discount eligible: true, Final total: 450.0
2) Border: 1000.0, "NO", "NO" -> Discount eligible: true, Final total: 900.0
3) Error: 300.0, "MAYBE", "NO" -> Error: invalid input
"""

print("\n--- PROBLEM 3: DISCOUNT ELIGIBILITY WITH BOOLEANS ---")

MIN_DISCOUNT_PURCHASE = 1000.0
DISCOUNT_MULTIPLIER = 0.90
MIN_PURCHASE_AMOUNT = 0.0

p3_totals = [500.0, 1000.0, 300.0]
p3_students = ["yes", "NO", "MAYBE"]
p3_seniors = ["no", "NO", "NO"]

for index in [0, 1, 2]:
    purchase_total = float(p3_totals[index])
    is_student_text = p3_students[index].strip().upper()
    is_senior_text = p3_seniors[index].strip().upper()

    valid_student_text = (is_student_text == "YES") or (is_student_text == "NO")
    valid_senior_text = (is_senior_text == "YES") or (is_senior_text == "NO")

    if purchase_total < MIN_PURCHASE_AMOUNT or not valid_student_text or not valid_senior_text:
        print("Error: invalid input")
    else:
        # Convert normalized strings to boolean flags
        is_student = bool(is_student_text == "YES")
        is_senior = bool(is_senior_text == "YES")

        discount_eligible = is_student or is_senior or (purchase_total >= MIN_DISCOUNT_PURCHASE)

        if discount_eligible:
            final_total = purchase_total * DISCOUNT_MULTIPLIER
        else:
            final_total = purchase_total

        print(f"Discount eligible: {str(discount_eligible).lower()}")
        print(f"Final total: {round(final_total, 2)}")


# PROBLEM 4: BASIC STATISTICS OF THREE INTEGERS
"""
Problem 4: Basic statistics of three integers
Description:
Reads three integer numbers and calculates their sum, average (float), maximum
value, minimum value, and a boolean flag (all_even) that is True if all three
numbers are even.

Inputs:
- n1 (int)
- n2 (int)
- n3 (int)

Outputs:
- Sum: <sum_value>
- Average: <average_value>
- Max: <max_value>
- Min: <min_value>
- All even: true|false

Validations:
- Verify that all three values can be converted to int (negatives are allowed).

Test cases:
1) Normal: "4", "8", "12" -> Sum: 24, Average: 8.0, Max: 12, Min: 4, All even: true
2) Border: "-2", "0", "5" -> Sum: 3, Average: 1.0, Max: 5, Min: -2, All even: false
3) Error: "10", "abc", "4" -> Error: invalid input
"""

print("\n--- PROBLEM 4: BASIC STATISTICS OF THREE INTEGERS ---")

TOTAL_NUMBERS = 3
EVEN_DIVISOR = 2

p4_n1_list = ["4", "-2", "10"]
p4_n2_list = ["8", "0", "abc"]
p4_n3_list = ["12", "5", "4"]

for index in [0, 1, 2]:
    raw_n1 = p4_n1_list[index].strip()
    raw_n2 = p4_n2_list[index].strip()
    raw_n3 = p4_n3_list[index].strip()

    # Remove leading minus sign to validate integer digits
    valid_n1 = raw_n1.replace("-", "", 1).isdigit()
    valid_n2 = raw_n2.replace("-", "", 1).isdigit()
    valid_n3 = raw_n3.replace("-", "", 1).isdigit()

    if not valid_n1 or not valid_n2 or not valid_n3:
        print("Error: invalid input")
    else:
        n1 = int(raw_n1)
        n2 = int(raw_n2)
        n3 = int(raw_n3)

        sum_value = n1 + n2 + n3
        average_value = float(sum_value / TOTAL_NUMBERS)
        max_value = max(n1, n2, n3)
        min_value = min(n1, n2, n3)

        # Boolean flag: True only if all three integers are divisible by 2
        all_even = (
            (n1 % EVEN_DIVISOR == 0)
            and (n2 % EVEN_DIVISOR == 0)
            and (n3 % EVEN_DIVISOR == 0)
        )

        print(f"Sum: {sum_value}")
        print(f"Average: {round(average_value, 2)}")
        print(f"Max: {max_value}")
        print(f"Min: {min_value}")
        print(f"All even: {str(all_even).lower()}")


# PROBLEM 5: LOAN ELIGIBILITY (INCOME AND DEBT RATIO)
"""
Problem 5: Loan eligibility (income and debt ratio)
Description:
Calculates the relative debt ratio (monthly_debt / monthly_income) and determines
if a person is eligible for a loan based on minimum monthly income, maximum debt
ratio, and minimum credit score.

Inputs:
- monthly_income (float; monthly income)
- monthly_debt (float; monthly debt payments)
- credit_score (int; credit score)

Outputs:
- Debt ratio: <debt_ratio>
- Eligible: true|false

Validations:
- monthly_income > 0.0 (to avoid division by zero)
- monthly_debt >= 0.0
- credit_score >= 0

Test cases:
1) Normal: income = 12000.0, debt = 3000.0, score = 700 -> Debt ratio: 0.25, Eligible: true
2) Border: income = 8000.0, debt = 3200.0, score = 650 -> Debt ratio: 0.4, Eligible: true
3) Error: income = 0.0, debt = 1500.0, score = 700 -> Error: invalid input
"""

print("\n--- PROBLEM 5: LOAN ELIGIBILITY ---")

MIN_REQUIRED_INCOME = 8000.0
MAX_ALLOWED_DEBT_RATIO = 0.4
MIN_REQUIRED_SCORE = 650

p5_incomes = [12000.0, 8000.0, 0.0]
p5_debts = [3000.0, 3200.0, 1500.0]
p5_scores = [700, 650, 700]

for index in [0, 1, 2]:
    monthly_income = float(p5_incomes[index])
    monthly_debt = float(p5_debts[index])
    credit_score = int(p5_scores[index])

    if monthly_income <= 0.0 or monthly_debt < 0.0 or credit_score < 0:
        print("Error: invalid input")
    else:
        debt_ratio = monthly_debt / monthly_income

        # Boolean flag: True if all three financial requirements are satisfied
        eligible = (
            monthly_income >= MIN_REQUIRED_INCOME
            and debt_ratio <= MAX_ALLOWED_DEBT_RATIO
            and credit_score >= MIN_REQUIRED_SCORE
        )

        print(f"Debt ratio: {round(debt_ratio, 2)}")
        print(f"Eligible: {str(eligible).lower()}")


# PROBLEM 6: BODY MASS INDEX (BMI) AND CATEGORY FLAG
"""
Problem 6: Body Mass Index (BMI) and category flag
Description:
Calculates a person's Body Mass Index (BMI) using weight in kilograms and height
in meters, rounds the result to 2 decimal places, and sets boolean flags for
underweight, normal weight, and overweight categories.

Inputs:
- weight_kg (float; weight in kilograms)
- height_m (float; height in meters)

Outputs:
- BMI: <bmi_rounded>
- Underweight: true|false
- Normal: true|false
- Overweight: true|false

Validations:
- weight_kg > 0.0
- height_m > 0.0 (also prevents division by zero)

Test cases:
1) Normal: weight_kg = 70.0, height_m = 1.75 -> BMI: 22.86, Underweight: false, Normal: true, Overweight: false
2) Border: weight_kg = 72.25, height_m = 1.70 -> BMI: 25.0, Underweight: false, Normal: false, Overweight: true
3) Error: weight_kg = 70.0, height_m = 0.0 -> Error: invalid input
"""

print("\n--- PROBLEM 6: BODY MASS INDEX (BMI) AND CATEGORY FLAG ---")

BMI_UNDERWEIGHT_LIMIT = 18.5
BMI_OVERWEIGHT_LIMIT = 25.0
ROUND_DECIMALS = 2

p6_weights = [70.0, 72.25, 70.0]
p6_heights = [1.75, 1.70, 0.0]

for index in [0, 1, 2]:
    weight_kg = float(p6_weights[index])
    height_m = float(p6_heights[index])

    if weight_kg <= 0.0 or height_m <= 0.0:
        print("Error: invalid input")
    else:
        bmi = weight_kg / (height_m * height_m)
        bmi_rounded = round(bmi, ROUND_DECIMALS)

        # Boolean flags for each BMI category using chained comparisons
        is_underweight = bool(bmi < BMI_UNDERWEIGHT_LIMIT)
        is_normal = bool(BMI_UNDERWEIGHT_LIMIT <= bmi < BMI_OVERWEIGHT_LIMIT)
        is_overweight = bool(bmi >= BMI_OVERWEIGHT_LIMIT)

        print(f"BMI: {bmi_rounded}")
        print(f"Underweight: {str(is_underweight).lower()}")
        print(f"Normal: {str(is_normal).lower()}")
        print(f"Overweight: {str(is_overweight).lower()}")


# CONCLUSIONS / CONCLUSIONES
"""
Working with integers (int) and floating-point numbers (float) together is
essential for solving real-world problems, where whole numbers represent counts
or scores and decimals represent money, temperatures, or physical measurements.
Relational operators allow us to compare these numeric values and produce boolean
flags (True or False) that drive decision-making structures with if-else blocks.
Validating ranges beforehand is critical to prevent mathematical errors like
division by zero and to reject impossible negative numbers. Furthermore, combining
multiple conditions with logical operators (and, or, not) makes it easy to model
practical rules used in payroll systems, store discounts, bank loans, and health
indicators.
"""

# REFERENCES / REFERENCIAS
"""
References:
1) Python Software Foundation. (2026). Built-in Types: Numeric Types — int, float, complex.
2) Python Software Foundation. (2026). Built-in Types: Truth Value Testing and Boolean Operations.
3)Python Software Foundation. (2026). Built-in Functions: int(), float(), bool(), round(), min(), max().
4) Matthes, E. (2023). Python Crash Course: A Hands-On, Project-Based Introduction
   to Programming (3rd ed.).
5) Sweigart, A. (2020). Automate the Boring Stuff with Python: Practical Programming
   for Total Beginners (2nd ed.).
"""