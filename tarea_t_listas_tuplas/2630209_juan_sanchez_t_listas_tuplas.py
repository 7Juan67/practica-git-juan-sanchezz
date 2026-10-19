# STUDENT INFORMATION / PORTADA
"""
Student Name: Juan Jassiel Sanchez Melendez
Student ID (Matricula): 2630209
Group: IM 1 - 2
GitHub Repository: https://github.com/7Juan67/practica-git-juan-sanchezz
"""

# EXECUTIVE SUMMARY / RESUMEN EJECUTIVO
"""
In Python, collections allow us to group and process multiple elements under a single
variable name. A list (list) is an ordered and mutable collection, meaning we can add,
remove, or modify its elements after creation using methods like append(), insert(),
remove(), or pop(). On the other hand, a tuple (tuple) is an ordered but immutable
collection, meaning its elements cannot be altered once defined, making it ideal for
fixed records such as 2D coordinates or configuration values. This document covers
problem descriptions, input and output design, data validations, and practical
implementations of lists and tuples tested with normal, border, and error cases.
"""

# PRINCIPLES AND BEST PRACTICES / PRINCIPIOS Y BUENAS PRACTICAS
"""
1. Use lists when you need to frequently add, remove, or sort elements.
2. Use tuples for fixed data that must not change (such as coordinates or dates).
3. Avoid modifying a list directly while iterating over it with a for loop.
4. Always validate that lists are not empty before calculating min(), max(), or averages.
5. Verify that index positions are within valid boundaries using len().
6. Write readable code using lower_snake_case variables and UPPER_SNAKE_CASE constants.
"""


# PROBLEM 1: SHOPPING LIST BASICS (LIST OPERATIONS)
"""
Problem 1: Shopping list basics (list operations)
Description:
Creates an initial shopping list from a comma-separated string, cleans extra
spaces for each product, appends a new item at the end, displays the total
number of items, and checks whether a specific product is inside the list.

Inputs:
- initial_items_text (string; e.g., "apple,banana,orange")
- new_item (string; product to add)
- search_item (string; product to search for)

Outputs:
- Items list: <items_list>
- Total items: <len_list>
- Found item: true|false

Validations:
- initial_items_text, new_item, and search_item must not be empty after strip().
- Split initial string by commas and strip spaces from each item.
- Reject empty items inside the initial list.

Test cases:
1) Normal: "apple, banana, orange", new: "grape", search: "banana" -> 4 items, Found: true
2) Border: "  milk  ", new: "bread", search: "eggs" -> 2 items, Found: false
3) Error: "   ", new: "apple", search: "apple" -> Error: invalid input
"""

print("--- PROBLEM 1: SHOPPING LIST BASICS ---")

MIN_TEXT_LENGTH = 1

p1_initial_texts = ["apple, banana, orange", "  milk  ", "   "]
p1_new_items = ["grape", "bread", "apple"]
p1_search_items = ["banana", "eggs", "apple"]

for index in [0, 1, 2]:
    initial_items_text = p1_initial_texts[index].strip()
    new_item = p1_new_items[index].strip().lower()
    search_item = p1_search_items[index].strip().lower()

    if (
        len(initial_items_text) < MIN_TEXT_LENGTH
        or len(new_item) < MIN_TEXT_LENGTH
        or len(search_item) < MIN_TEXT_LENGTH
    ):
        print("Error: invalid input")
    else:
        raw_items_list = initial_items_text.split(",")
        items_list = []

        # Clean each individual product and add valid ones to items_list
        for raw_item in raw_items_list:
            clean_item = raw_item.strip().lower()
            if len(clean_item) >= MIN_TEXT_LENGTH:
                items_list.append(clean_item)

        if len(items_list) == 0:
            print("Error: invalid input")
        else:
            # Add the new product at the end of the shopping list
            items_list.append(new_item)

            total_items = len(items_list)
            is_in_list = bool(search_item in items_list)

            print(f"Items list: {items_list}")
            print(f"Total items: {total_items}")
            print(f"Found item: {str(is_in_list).lower()}")


# PROBLEM 2: POINTS AND DISTANCES WITH TUPLES
"""
Problem 2: Points and distances with tuples
Description:
Uses immutable tuples to represent two 2D points (x1, y1) and (x2, y2).
Calculates the Euclidean distance between both points and creates a new
tuple representing the midpoint (mx, my).

Inputs:
- x1, y1, x2, y2 (float; coordinates of Point A and Point B)

Outputs:
- Point A: (x1, y1)
- Point B: (x2, y2)
- Distance: <distance>
- Midpoint: (mx, my)

Validations:
- Verify that all 4 coordinate inputs can be converted to float.

Test cases:
1) Normal: x1="0.0", y1="0.0", x2="3.0", y2="4.0" -> Distance: 5.0, Midpoint: (1.5, 2.0)
2) Border: x1="-2.0", y1="5.0", x2="-2.0", y2="5.0" -> Distance: 0.0, Midpoint: (-2.0, 5.0)
3) Error: x1="1.0", y1="abc", x2="3.0", y2="4.0" -> Error: invalid input
"""

print("\n--- PROBLEM 2: POINTS AND DISTANCES WITH TUPLES ---")

X_INDEX = 0
Y_INDEX = 1
SQUARE_EXPONENT = 2
SQRT_EXPONENT = 0.5
MIDPOINT_DIVISOR = 2.0
ROUND_DECIMALS = 2

p2_x1_list = ["0.0", "-2.0", "1.0"]
p2_y1_list = ["0.0", "5.0", "abc"]
p2_x2_list = ["3.0", "-2.0", "3.0"]
p2_y2_list = ["4.0", "5.0", "4.0"]

for index in [0, 1, 2]:
    raw_x1 = p2_x1_list[index].strip()
    raw_y1 = p2_y1_list[index].strip()
    raw_x2 = p2_x2_list[index].strip()
    raw_y2 = p2_y2_list[index].strip()

    # Validate that all 4 strings represent valid float numbers
    valid_x1 = raw_x1.replace("-", "", 1).replace(".", "", 1).isdigit()
    valid_y1 = raw_y1.replace("-", "", 1).replace(".", "", 1).isdigit()
    valid_x2 = raw_x2.replace("-", "", 1).replace(".", "", 1).isdigit()
    valid_y2 = raw_y2.replace("-", "", 1).replace(".", "", 1).isdigit()

    if not valid_x1 or not valid_y1 or not valid_x2 or not valid_y2:
        print("Error: invalid input")
    else:
        x1 = float(raw_x1)
        y1 = float(raw_y1)
        x2 = float(raw_x2)
        y2 = float(raw_y2)

        # Create immutable tuples for both 2D points
        point_a = (x1, y1)
        point_b = (x2, y2)

        # Access coordinates via tuple indexing [0] and [1]
        delta_x = point_b[X_INDEX] - point_a[X_INDEX]
        delta_y = point_b[Y_INDEX] - point_a[Y_INDEX]

        distance = ((delta_x ** SQUARE_EXPONENT) + (delta_y ** SQUARE_EXPONENT)) ** SQRT_EXPONENT

        mid_x = round((point_a[X_INDEX] + point_b[X_INDEX]) / MIDPOINT_DIVISOR, ROUND_DECIMALS)
        mid_y = round((point_a[Y_INDEX] + point_b[Y_INDEX]) / MIDPOINT_DIVISOR, ROUND_DECIMALS)
        midpoint = (mid_x, mid_y)

        print(f"Point A: {point_a}")
        print(f"Point B: {point_b}")
        print(f"Distance: {round(distance, ROUND_DECIMALS)}")
        print(f"Midpoint: {midpoint}")


# CONCLUSIONS / CONCLUSIONES
"""
Using collections in Python makes it much easier to organize and process groups
of data instead of creating dozens of separate variables. Lists are ideal when
a program needs flexibility to add new elements with append(), remove items, or
search for values dynamically using the 'in' operator. On the other hand, tuples
provide safety for data that should remain constant throughout execution, such
as 2D coordinates (x, y) in engineering calculations. Validating inputs before
converting types or accessing collection elements prevents execution errors and
ensures accurate results.
"""

# REFERENCES / REFERENCIAS
"""
References:
1) Python Software Foundation. (2026). Built-in Types: Sequence Types — list, tuple, range.
2) Python Software Foundation. (2026). More on Lists and Tuples — Python Tutorial.
3) Matthes, E. (2023). Python Crash Course: A Hands-On, Project-Based Introduction
   to Programming (3rd ed.).
4) Sweigart, A. (2020). Automate the Boring Stuff with Python: Practical Programming
   for Total Beginners (2nd ed.).
5) Real Python. (2025). Lists and Tuples in Python.
"""