"""
Student Name: Juan Jassiel Sanchez Melendez
Student ID (Matricula): 2630209
Group: IM 1 - 2
GitHub Repository: https://github.com/7Juan67/practica-git-juan-sanchezz
"""

# EXECUTIVE SUMMARY / RESUMEN EJECUTIVO
"""
In Python, a string (str) is an immutable sequence of characters used to represent text.
Immutability means that once a string is created in memory, it cannot be changed directly;
every operation produces a completely new string. Basic operations include concatenation (+),
repetition (*), measuring length with len(), extracting parts using slicing [a:b], searching
with find() or in, and replacing characters with replace(). Validating and normalizing user
inputs (like names, emails, and passwords) is important to avoid errors and keep data clean
and consistent. This document contains 6 problems demonstrating input validation, string
methods, output formatting, and three test cases (normal, border, and error) for each problem.
"""

# PRINCIPLES AND BEST PRACTICES / PRINCIPIOS Y BUENAS PRACTICAS
"""
1. Strings are immutable: any change or method generates a new string in memory.
2. Always normalize user input with strip() and lower() before making comparisons.
3. Avoid magic numbers in slices or indexes; use UPPER_SNAKE_CASE constants instead.
4. Use built-in string methods like split(), join(), and replace() instead of manual logic.
5. Design clear validations: first verify the string is not empty, then check the format.
6. Write readable code with lower_snake_case variables and clear English messages.
"""



# PROBLEM 1: FULL NAME FORMATTER (NAME + INITIALS)
"""
Problem 1: Full name formatter (name + initials)
Description:
Receives a full name string, removes extra spaces, formats the text into
Title Case, and generates the person's initials separated by dots.

Inputs:
- full_name (string)

Outputs:
- Formatted name: <Name In Title Case>
- Initials: <X.X.X.>

Validations:
- full_name must not be empty after applying strip().
- Must have at least 2 words after splitting by spaces.

Test cases:
1) Normal: "juan carlos tovar" -> Formatted name: Juan Carlos Tovar, Initials: J.C.T.
2) Border: "   luis   angel   " -> Formatted name: Luis Angel, Initials: L.A.
3) Error: "   carlos   " or "   " -> Error: invalid input
"""

print("--- PROBLEM 1: FULL NAME FORMATTER ---")

MIN_WORDS_NAME = 2
FIRST_LETTER_INDEX = 0

p1_test_cases = ["juan carlos tovar", "   luis   angel   ", "   carlos   "]

for full_name in p1_test_cases:
    clean_name = full_name.strip()

    if len(clean_name) == 0:
        print("Error: invalid input")
    else:
        word_list = clean_name.split()

        if len(word_list) < MIN_WORDS_NAME:
            print("Error: invalid input")
        else:
            formatted_name = " ".join(word_list).title()

            # Build initials using string concatenation (+) and indexing [0]
            initials_text = ""
            for word in word_list:
                initials_text = initials_text + word[FIRST_LETTER_INDEX].upper() + "."

            print(f"Formatted name: {formatted_name}")
            print(f"Initials: {initials_text}")



# PROBLEM 2: SIMPLE EMAIL VALIDATOR (STRUCTURE + DOMAIN)
"""
Problem 2: Simple email validator (structure + domain)
Description:
Checks if an email address has a valid basic format (no spaces, exactly one '@',
and at least one '.' in the domain part) and displays the domain if valid.

Inputs:
- email_text (string)

Outputs:
- Valid email: true / false
- Domain: <domain_part> (only if valid)

Validations:
- email_text must not be empty after strip().
- Must not contain spaces (" " not in email_text).
- Must contain one '@' and have text before and after it.

Test cases:
1) Normal: "contacto@upvictoria.edu.mx" -> Valid email: true, Domain: upvictoria.edu.mx
2) Border: "  u@d.co  " -> Valid email: true, Domain: d.co
3) Error: "correo sin arroba.com" -> Valid email: false
"""

print("\n--- PROBLEM 2: SIMPLE EMAIL VALIDATOR ---")

REQUIRED_AT_COUNT = 1

p2_test_cases = ["contacto@upvictoria.edu.mx", "  u@d.co  ", "correo sin arroba.com"]

for email_text in p2_test_cases:
    clean_email = email_text.strip()

    if len(clean_email) == 0:
        print("Error: invalid input")
    elif " " in clean_email or clean_email.count("@") != REQUIRED_AT_COUNT:
        print("Valid email: false")
    else:
        at_position = clean_email.find("@")
        user_part = clean_email[:at_position]
        domain_part = clean_email[at_position + 1 :]

        if (
            len(user_part) == 0
            or "." not in domain_part
            or domain_part.startswith(".")
            or domain_part.endswith(".")
        ):
            print("Valid email: false")
        else:
            print("Valid email: true")
            print(f"Domain: {domain_part}")


# PROBLEM 3: PALINDROME CHECKER (IGNORING SPACES AND CASE)
"""
Problem 3: Palindrome checker (ignoring spaces and case)
Description:
Checks if a phrase reads the same from left to right and from right to left,
ignoring blank spaces and uppercase/lowercase letters.

Inputs:
- phrase (string)

Outputs:
- Normalized phrase: <clean_text>
- Is palindrome: true / false

Validations:
- phrase must not be empty after strip().
- Must have at least 3 characters after removing all spaces.

Test cases:
1) Normal: "Anita lava la tina" -> Is palindrome: true
2) Border: "  O s o  " -> Is palindrome: true
3) Error: " a b " -> Error: invalid input
"""

print("\n--- PROBLEM 3: PALINDROME CHECKER ---")

MIN_PALINDROME_LEN = 3

p3_test_cases = ["Anita lava la tina", "  O s o  ", " a b "]

for phrase in p3_test_cases:
    clean_phrase = phrase.strip()

    if len(clean_phrase) == 0:
        print("Error: invalid input")
    else:
        normalized_phrase = clean_phrase.lower().replace(" ", "")

        if len(normalized_phrase) < MIN_PALINDROME_LEN:
            print("Error: invalid input")
        else:
            reversed_phrase = normalized_phrase[::-1]
            print(f"Normalized phrase: {normalized_phrase}")

            if normalized_phrase == reversed_phrase:
                print("Is palindrome: true")
            else:
                print("Is palindrome: false")


# PROBLEM 4: SENTENCE WORD STATS (LENGTHS AND FIRST/LAST WORD)
"""
Problem 4: Sentence word stats (lengths and first/last word)
Description:
Normalizes outer spaces of a sentence, splits it into words, and shows the total
word count, the first word, the last word, the shortest word, and the longest word.

Inputs:
- sentence (string)

Outputs:
- Word count: <n>
- First word: <...>
- Last word: <...>
- Shortest word: <...>
- Longest word: <...>

Validations:
- sentence must not be empty after strip().
- Must contain at least one word after split().

Test cases:
1) Normal: "Mechatronics uses sensors and microcontrollers" -> Prints 5 words stats
2) Border: "   Arduino   " -> Prints stats for 1 single word
3) Error: "     " -> Error: invalid input
"""

print("\n--- PROBLEM 4: SENTENCE WORD STATS ---")

FIRST_INDEX = 0
LAST_INDEX = -1

p4_test_cases = [
    "Mechatronics uses sensors and microcontrollers",
    "   Arduino   ",
    "     ",
]

for sentence in p4_test_cases:
    clean_sentence = sentence.strip()

    if len(clean_sentence) == 0:
        print("Error: invalid input")
    else:
        words_in_sentence = clean_sentence.split()
        total_words = len(words_in_sentence)

        if total_words == 0:
            print("Error: invalid input")
        else:
            first_word = words_in_sentence[FIRST_INDEX]
            last_word = words_in_sentence[LAST_INDEX]
            shortest_word = words_in_sentence[FIRST_INDEX]
            longest_word = words_in_sentence[FIRST_INDEX]

            for current_word in words_in_sentence:
                if len(current_word) < len(shortest_word):
                    shortest_word = current_word
                if len(current_word) > len(longest_word):
                    longest_word = current_word

            print(f"Word count: {total_words}")
            print(f"First word: {first_word}")
            print(f"Last word: {last_word}")
            print(f"Shortest word: {shortest_word}")
            print(f"Longest word: {longest_word}")


# PROBLEM 5: PASSWORD STRENGTH CLASSIFIER
"""
Problem 5: Password strength classifier
Description:
Classifies a password as 'weak', 'medium', or 'strong' by checking its length
and verifying if it has uppercase, lowercase, digits, and symbols.
Rules:
- Strong: length >= 8 and has upper, lower, digit, and symbol.
- Medium: length >= 8 and combines letters (upper/lower) or digits.
- Weak: length < 8 or only has a single type of character (e.g. only lowercase).

Inputs:
- password_input (string)

Outputs:
- Password strength: weak / medium / strong

Validations:
- password_input must not be empty after strip().

Test cases:
1) Normal: "Mecha2026#Bot" -> Password strength: strong
2) Border: "Robot123" -> Password strength: medium (exact length 8, no symbol)
3) Error: "   " -> Error: invalid input
"""

print("\n--- PROBLEM 5: PASSWORD STRENGTH CLASSIFIER ---")

MIN_PASSWORD_LEN = 8

p5_test_cases = ["Mecha2026#Bot", "Robot123", "   "]

for password_input in p5_test_cases:
    clean_password = password_input.strip()

    if len(clean_password) == 0:
        print("Error: invalid input")
    else:
        password_len = len(clean_password)
        has_upper = False
        has_lower = False
        has_digit = False
        has_symbol = False

        for char in clean_password:
            if char.isupper():
                has_upper = True
            elif char.islower():
                has_lower = True
            elif char.isdigit():
                has_digit = True
            elif not char.isalnum():
                has_symbol = True

        if password_len < MIN_PASSWORD_LEN:
            strength_level = "weak"
        elif has_upper and has_lower and has_digit and has_symbol:
            strength_level = "strong"
        elif (has_upper and has_lower) or (has_lower and has_digit) or (has_upper and has_digit):
            strength_level = "medium"
        else:
            strength_level = "weak"

        print(f"Password strength: {strength_level}")


# PROBLEM 6: PRODUCT LABEL FORMATTER (FIXED-WIDTH TEXT)
"""
Problem 6: Product label formatter (fixed-width text)
Description:
Creates a product label with the format 'Product: <NAME> | Price: $<PRICE>'
and adjusts its size so the final text always has an exact length of 30 characters.

Inputs:
- product_name (string)
- price_value (string)

Outputs:
- Label: "<exactly 30 characters>"
- Length: 30

Validations:
- product_name must not be empty after strip().
- price_value must be a valid positive number (checked with replace and isdigit).

Test cases:
1) Normal: "Servo Motor", "85.5" -> Padded with spaces up to 30 chars
2) Border: "Microcontroller Board ESP32 WiFi", "150" -> Truncated to 30 chars
3) Error: "LED", "-10" -> Error: invalid input
"""

print("\n--- PROBLEM 6: PRODUCT LABEL FORMATTER ---")

FIXED_LABEL_WIDTH = 30

p6_names = ["Servo Motor", "Microcontroller Board ESP32 WiFi", "LED"]
p6_prices = ["85.5", "150", "-10"]

for index in [0, 1, 2]:
    product_name = p6_names[index].strip()
    price_value = p6_prices[index].strip()

    # Check if price is a positive number by removing one dot and using isdigit()
    price_digits_only = price_value.replace(".", "", 1)

    if len(product_name) == 0 or len(price_value) == 0 or not price_digits_only.isdigit():
        print("Error: invalid input")
    else:
        price_number = float(price_value)

        if price_number <= 0:
            print("Error: invalid input")
        else:
            base_label = f"Product: {product_name} | Price: ${price_number:.2f}"

            if len(base_label) > FIXED_LABEL_WIDTH:
                # Cut the string to 30 characters using slicing
                final_label = base_label[:FIXED_LABEL_WIDTH]
            else:
                # Fill remaining characters with spaces using repetition (*)
                spaces_needed = FIXED_LABEL_WIDTH - len(base_label)
                final_label = base_label + (" " * spaces_needed)

            print(f'Label: "{final_label}"')
            print(f"Length: {len(final_label)}")


# CONCLUSIONS / CONCLUSIONES
"""
Handling strings is essential in programming because most user inputs and program
outputs are text-based. Using methods like strip() and lower() makes it easy to
clean accidental spaces and standardize letters before comparing two strings.
Similarly, split() and join() simplify breaking sentences into words and putting
them back together cleanly. Designing validations at the start of every program
prevents execution crashes and stops invalid data from producing wrong results.
Finally, working through these exercises showed how string immutability requires
saving every modified string into a variable, and how slicing [a:b] helps extract
or trim text accurately.
"""


# REFERENCES / REFERENCIAS
"""
References:
1) Python Software Foundation. (2026). Built-in Types: Text Sequence Type — str.
2) Python Software Foundation. (2026). String Methods — Python 3 Documentation.
3) Matthes, E. (2023). Python Crash Course: A Hands-On, Project-Based Introduction
   to Programming (3rd ed.).
4) Sweigart, A. (2020). Automate the Boring Stuff with Python: Practical Programming
   for Total Beginners (2nd ed.).
5) Real Python. (2025). Strings and Character Data in Python.
"""