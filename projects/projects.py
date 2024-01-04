import math
import re


# Hello, World!
# Write a Python program that prints "Hello, World!" to the console.
def hello():
    print("Hello, World!")


# Calculate the Area of a Circle
# Write a program that takes the radius of a circle as input and calculates its area. Use the formula: area = pi * r * r (where pi is a constant).
def calculate_circle_area(radius):
    if radius < 0:
        return "Radius cannot be negative."
    else:
        area = math.pi * radius * radius
        return area


# Sum of Even Numbers
# Write a program that calculates and prints the sum of all even numbers from 1 to 100.
def sum_of_even_numbers():
    even_sum = 0
    # Start from 2 and go up to 100 in steps of 2 (even numbers)
    for number in range(2, 101, 2):
        even_sum += number
    return even_sum


# Write a program that computes the factorial of a given number using a loop.
def factorial(n):
    if n < 0:
        return "Factorial is not defined for negative numbers."
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result


# Create a program that takes a string as input and prints the reverse of that string.
def reverse_string(input_string):
    reversed_string = input_string[::-1]
    return reversed_string


# Write a program that checks if a given number is prime or not.
def is_prime(number):
    if number <= 1:
        return False
    elif number <= 3:
        return True
    elif number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


# Implement the FizzBuzz problem: For numbers from 1 to 100, print "Fizz" if the number is divisible by 3, "Buzz" if divisible by 5,
# and "FizzBuzz" if divisible by both 3 and 5. Otherwise, print the number.
def fizz_buzz():
    for num in range(1, 101):
        if num % 3 == 0 and num % 5 == 0:
            print("FizzBuzz")
        elif num % 3 == 0:
            print("Fizz")
        elif num % 5 == 0:
            print("Buzz")
        else:
            print(num)


# Count Words in a String
# Write a program that counts the number of words in a given string. Assume words are separated by spaces.
def count_words(input_string):
    # Split the input string by spaces and count the number of resulting elements
    words = input_string.split()
    return len(words)


# Find the Largest Element
# Write a program that finds and prints the largest element in a list of numbers.
def find_largest(numbers):
    if not numbers:
        return None  # Return None for an empty list
    largest = numbers[0]
    for num in numbers:
        if num > largest:
            largest = num
    return largest


# Palindrome Checker
# Create a program that checks if a given string is a palindrome (reads the same forwards and backwards).
def is_palindrome(input_string):
    # Remove spaces and convert the string to lowercase for case-insensitive comparison
    cleaned_string = input_string.replace(" ", "").lower()
    # Check if the cleaned string is equal to its reverse
    return cleaned_string == cleaned_string[::-1]


# Sum of Digits
# Write a program that takes an integer as input and calculates the sum of its digits.
def sum_of_digits(number):
    # Ensure the input is a positive integer
    if not isinstance(number, int) or number < 0:
        return "Invalid input. Please enter a positive integer."

    # Convert the number to a string to easily iterate through its digits
    number_str = str(number)

    # Calculate the sum of digits
    digit_sum = 0
    for digit in number_str:
        digit_sum += int(digit)

    return digit_sum


# Leap Year Checker
# Create a program that checks if a given year is a leap year. Leap years are divisible by 4 but not divisible by 100 unless they are also divisible by 400.
def is_leap_year(year):
    if not isinstance(year, int) or year < 0:
        raise ValueError("Invalid input. Please enter a positive integer.")
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False


# Multiplication Table
# Write a program that generates and prints the multiplication table for a given number (up to a certain range).
def generate_multiplication_table(number, up_to_range):
    if number <= 0 or up_to_range <= 0:
        return "Invalid input. Both number and range should be positive integers."

    table = []
    for i in range(1, up_to_range + 1):
        product = number * i
        table.append(f"{number} x {i} = {product}")

    return table


# GCD (Greatest Common Divisor)
# Implement a program that finds and prints the greatest common divisor of two given numbers.
def find_gcd(a, b):
    if a < 0 or b < 0:
        raise ValueError("Invalid input. Please enter positive integers.")

    while b:
        a, b = b, a % b
    return a


# Power of a Number
# Write a program that calculates the result of raising a number to a given power (both inputs provided by the user).
def calculate_power(base, exponent):
    result = base**exponent
    return result


# List Reversal
# Create a program that reverses a list without using any built-in functions.
def reverse_list(input_list):
    reversed_list = []
    for item in input_list:
        reversed_list.insert(0, item)
    return reversed_list


# Remove Duplicates
# Write a program that removes duplicates from a list while preserving the order of the original list.
def remove_duplicates(input_list):
    unique_list = []
    for item in input_list:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list


# Count Vowels and Consonants
# Implement a program that counts the number of vowels and consonants in a given string (case-insensitive).
def count_vowels_and_consonants(input_string):
    # Convert the input string to lowercase for case-insensitive comparison
    input_string = input_string.lower()
    vowels = "aeiou"
    vowel_count = 0
    consonant_count = 0

    for char in input_string:
        if char.isalpha():
            if char in vowels:
                vowel_count += 1
            else:
                consonant_count += 1

    return vowel_count, consonant_count


# Prime Number Generator
# Write a program that generates and prints a list of prime numbers within a given range.
def is_prime(number):
    if number <= 1:
        return False
    if number <= 3:
        return True
    if number % 2 == 0 or number % 3 == 0:
        return False
    i = 5
    while i * i <= number:
        if number % i == 0 or number % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_primes_in_range_slow(start, end):
    if start < 0 or end < 0:
        raise ValueError(
            "Invalid input. Both start and end should be positive integers."
        )

    if start > end:
        raise ValueError("Invalid input. Start should be less than or equal to end.")

    prime_list = []
    for num in range(start, end + 1):
        if is_prime(num):
            prime_list.append(num)
    return prime_list


# Palindrome List
# Write a program that takes a list of strings as input and returns a new list containing only the palindromes from the original list.
def filter_palindromes(word_list):
    palindrome_list = [word for word in word_list if is_palindrome(word)]
    return palindrome_list


# Fibonacci Sequence
# Create a program that generates and prints the first n numbers in the Fibonacci sequence, where n is given as input.
def generate_fibonacci_sequence(n):
    fibonacci_sequence = []
    if n <= 0:
        return fibonacci_sequence
    elif n == 1:
        return [0]
    elif n == 2:
        return [0, 1]
    else:
        fibonacci_sequence = [0, 1]
        for i in range(2, n):
            next_number = fibonacci_sequence[-1] + fibonacci_sequence[-2]
            fibonacci_sequence.append(next_number)
        return fibonacci_sequence


# Anagram Checker
# Implement a program that checks if two strings are anagrams of each other (i.e., they have the same characters in different orders).
def are_anagrams(str1, str2):
    # Remove spaces and convert both strings to lowercase for case-insensitive comparison
    str1 = str1.replace(" ", "").lower()
    str2 = str2.replace(" ", "").lower()

    # Check if the sorted characters of both strings match
    return sorted(str1) == sorted(str2)


# Matrix Transposition
# Write a program that transposes a given matrix (2D list), switching rows with columns.
def transpose_matrix(matrix):
    if not matrix:
        return []
    num_rows = len(matrix)
    num_cols = len(matrix[0])

    transposed_matrix = [[0] * num_rows for _ in range(num_cols)]

    for i in range(num_rows):
        for j in range(num_cols):
            transposed_matrix[j][i] = matrix[i][j]

    return transposed_matrix


# Factorization
# Create a program that factors a given positive integer and prints its prime factors.
def factor_integer(n):
    factors = []
    divisor = 2

    while n > 1:
        while n % divisor == 0:
            factors.append(divisor)
            n //= divisor
        divisor += 1

    return factors


# Reverse Words in a Sentence
# Write a program that reverses the words in a sentence. For example, "Hello, World!" should become "World! Hello,".


def reverse_words(sentence):
    words = sentence.split()
    reversed_sentence = " ".join(reversed(words))
    return reversed_sentence


# List Intersection
# Implement a program that finds and prints the common elements between two lists.
def find_common_elements(list1, list2):
    common_elements = list(set(list1) & set(list2))
    return common_elements


# Decimal to Binary Converter
# Create a program that converts a decimal number to its binary representation.
def decimal_to_binary(decimal):
    if decimal < 0:
        return "-" + decimal_to_binary(-decimal)
    elif decimal == 0:
        return "0"
    else:
        binary = ""
        while decimal > 0:
            binary = str(decimal % 2) + binary
            decimal //= 2
        return binary


# Sum of Squares vs. Square of Sum
# Write a program that calculates and prints the difference between the sum of squares and the square of the sum of the first n natural numbers, where n is given as input.
def sum_of_squares(n):
    return sum([i**2 for i in range(1, n + 1)])


def square_of_sum(n):
    return sum(range(1, n + 1)) ** 2


# Email Validator
# Implement a program that checks if a given string is a valid email address based on a simple set of rules (e.g., it contains an "@" symbol and a "." character in the right positions).
def is_valid_email(email):
    # Define a regular expression pattern to match a simple email address
    pattern = r"^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$"

    # Use the re.match() function to check if the email matches the pattern
    if re.match(pattern, email):
        return True
    else:
        return False


# Pascal's Triangle
# Write a program that generates and prints the first n rows of Pascal's Triangle, where n is given as input.
def generate_pascals_triangle(n):
    triangle = []

    for i in range(n):
        row = [1] if i == 0 else [1] + [row[j] + row[j + 1] for j in range(i - 1)] + [1]
        triangle.append(row)

    return triangle


def print_pascals_triangle(triangle):
    max_width = len(" ".join(map(str, triangle[-1])))

    for row in triangle:
        formatted_row = " ".join(map(str, row)).center(max_width)
        print(formatted_row)


# Matrix Multiplication
# Create a program that performs matrix multiplication for two given matrices and prints the result.
def matrix_multiply(matrix1, matrix2):
    if len(matrix1[0]) != len(matrix2):
        raise ValueError(
            "Number of columns in the first matrix must match the number of rows in the second matrix."
        )

    result = []
    for i in range(len(matrix1)):
        row = []
        for j in range(len(matrix2[0])):
            product = 0
            for k in range(len(matrix2)):
                product += matrix1[i][k] * matrix2[k][j]
            row.append(product)
        result.append(row)

    return result


def print_matrix(matrix):
    for row in matrix:
        print(" ".join(map(str, row)))


# Common Characters in Strings
# Write a program that finds and prints the common characters between two strings (case-sensitive).
def find_common_characters(string1, string2):
    common_characters = set(string1) & set(string2)
    return "".join(sorted(common_characters))


# Armstrong Number Checker
# Implement a program that checks if a given number is an Armstrong number. An Armstrong number is one where the sum of its own digits, each raised to the power of the number of digits, is equal to the number itself.
def is_armstrong_number(number):
    num_str = str(number)
    num_digits = len(num_str)
    sum_of_powers = sum(int(digit) ** num_digits for digit in num_str)
    return sum_of_powers == number


# String Compression
# Create a program that compresses a given string by replacing consecutive duplicate characters with the character followed by the count.
# Count should NOT be omitted even if it is 1.
def compress_string(input_string):
    if not input_string:
        return input_string

    compressed = []
    current_char = input_string[0]
    char_count = 1

    for char in input_string[1:]:
        if char == current_char:
            char_count += 1
        else:
            compressed.append(current_char + str(char_count))
            current_char = char
            char_count = 1

    compressed.append(current_char + str(char_count))
    compressed_string = "".join(compressed)

    return compressed_string


# String Compression 2
# Create a program that compresses a given string by replacing consecutive duplicate characters with the character followed by the count.
# Count should be omitted if it is 1.
def compress_string2(input_string):
    if not input_string:
        return input_string

    compressed = []
    current_char = input_string[0]
    char_count = 1

    for char in input_string[1:]:
        if char == current_char:
            char_count += 1
        else:
            if char_count == 1:
                compressed.append(current_char)
            else:
                compressed.append(current_char + str(char_count))
            current_char = char
            char_count = 1

    if char_count == 1:
        compressed.append(current_char)
    else:
        compressed.append(current_char + str(char_count))

    compressed_string = "".join(compressed)

    return compressed_string


# Count Substrings
# Create a program that counts the occurrences of a given substring within a larger string.
# You may use standard library functions.
def count_substring_occurrences(full_string, substring):
    count = 0
    start = 0

    while start < len(full_string):
        index = full_string.find(substring, start)
        if index == -1:
            break
        count += 1
        start = index + 1

    return count


# Largest Palindrome Product
# Write a program that finds and prints the largest palindrome that is a product of two three-digit numbers.
def find_largest_palindrome_product():
    largest_palindrome = 0

    for i in range(999, 99, -1):
        for j in range(i, 99, -1):
            product = i * j
            if is_palindrome(str(product)) and product > largest_palindrome:
                largest_palindrome = product

    return largest_palindrome


# Sum of Primes
# Create a program that calculates and prints the sum of all prime numbers below a given limit.
def sum_primes_below_limit(limit):
    prime_sum = 0
    for number in range(2, limit):
        if is_prime(number):
            prime_sum += number
    return prime_sum


# Quadratic Equation Solver
# Write a program that takes coefficients (a, b, and c) of a quadratic equation as input and calculates its real roots using the quadratic formula.
def calculate_quadratic_roots(a, b, c):
    discriminant = b**2 - 4 * a * c

    if discriminant > 0:
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return root1, root2
    elif discriminant == 0:
        root = -b / (2 * a)
        return (root,)
    else:
        return None  # No real roots


# Remove Duplicates from Sorted Array
# Implement a program that removes duplicates from a sorted list in-place and returns the new length of the modified list.
def remove_duplicates(nums):
    if not nums:
        return 0

    new_length = 1  # Initialize with the first element
    for i in range(1, len(nums)):
        if nums[i] != nums[i - 1]:
            nums[new_length] = nums[i]
            new_length += 1

    return new_length


# Vigenère Cipher
# Implement a program that encrypts and decrypts messages using the Vigenère cipher. Allow the user to input a keyword for encryption and decryption.
def vigenere_encrypt(plain_text, keyword):
    encrypted_text = ""
    keyword = keyword.upper()
    keyword_length = len(keyword)
    index = 0

    for char in plain_text:
        if char.isalpha():
            shift = ord(keyword[index % keyword_length]) - ord("A")
            if char.islower():
                encrypted_char = chr(((ord(char) - ord("a") + shift) % 26) + ord("a"))
            else:
                encrypted_char = chr(((ord(char) - ord("A") + shift) % 26) + ord("A"))
            index += 1
        else:
            encrypted_char = char
        encrypted_text += encrypted_char

    return encrypted_text


def vigenere_decrypt(encrypted_text, keyword):
    decrypted_text = ""
    keyword = keyword.upper()
    keyword_length = len(keyword)
    index = 0

    for char in encrypted_text:
        if char.isalpha():
            shift = ord(keyword[index % keyword_length]) - ord("A")
            if char.islower():
                decrypted_char = chr(((ord(char) - ord("a") - shift) % 26) + ord("a"))
            else:
                decrypted_char = chr(((ord(char) - ord("A") - shift) % 26) + ord("A"))
            index += 1
        else:
            decrypted_char = char
        decrypted_text += decrypted_char

    return decrypted_text


# Caesar Cipher
# Create a program that encrypts and decrypts messages using a Caesar cipher. Allow the user to specify the shift value.
def caesar_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                encrypted_char = chr(((ord(char) - ord("a") + shift) % 26) + ord("a"))
            else:
                encrypted_char = chr(((ord(char) - ord("A") + shift) % 26) + ord("A"))
        else:
            encrypted_char = char
        encrypted_text += encrypted_char
    return encrypted_text


def caesar_decrypt(text, shift):
    decrypted_text = ""
    for char in text:
        if char.isalpha():
            if char.islower():
                decrypted_char = chr(((ord(char) - ord("a") - shift) % 26) + ord("a"))
            else:
                decrypted_char = chr(((ord(char) - ord("A") - shift) % 26) + ord("A"))
        else:
            decrypted_char = char
        decrypted_text += decrypted_char
    return decrypted_text
