import math
import re


# Hello, World!
# Write a Python program that prints "Hello, World!" to the console.
def hello():
    # TODO: Your code here
    return


# Calculate the Area of a Circle
# Write a program that takes the radius of a circle as input and calculates its area. Use the formula: area = pi * r * r (where pi is a constant).
def calculate_circle_area(radius):
    # TODO: Your code here
    return


# Sum of Even Numbers
# Write a program that calculates and prints the sum of all even numbers from 1 to 100.
def sum_of_even_numbers():
    even_sum = 0
    # TODO: Your code here
    return even_sum


# Write a program that computes the factorial of a given number using a loop.
def factorial(n):
    # TODO: Your code here
    return


# Create a program that takes a string as input and prints the reverse of that string.
def reverse_string(input_string):
    # TODO: Your code here
    return


# Write a program that checks if a given number is prime or not.
def is_prime(number):
    # TODO: Your code here
    return


# Implement the FizzBuzz problem: For numbers from 1 to 100, print "Fizz" if the number is divisible by 3, "Buzz" if divisible by 5,
# and "FizzBuzz" if divisible by both 3 and 5. Otherwise, print the number.
def fizz_buzz():
    # TODO: Your code here
    return


# Count Words in a String
# Write a program that counts the number of words in a given string. Assume words are separated by spaces.
def count_words(input_string):
    # TODO: Your code here
    return


# Find the Largest Element
# Write a program that finds and prints the largest element in a list of numbers.
def find_largest(numbers):
    # TODO: Your code here
    return


# Palindrome Checker
# Create a program that checks if a given string is a palindrome (reads the same forwards and backwards).
def is_palindrome(input_string):
    # TODO: Your code here
    return


# Sum of Digits
# Write a program that takes an integer as input and calculates the sum of its digits.
def sum_of_digits(number):
    # TODO: Your code here
    return


# Leap Year Checker
# Create a program that checks if a given year is a leap year. Leap years are divisible by 4 but not divisible by 100 unless they are also divisible by 400.
def is_leap_year(year):
    # TODO: Your code here
    return


# Multiplication Table
# Write a program that generates and prints the multiplication table for a given number (up to a certain range).
def generate_multiplication_table(number, up_to_range):
    # TODO: Your code here
    return


# GCD (Greatest Common Divisor)
# Implement a program that finds and prints the greatest common divisor of two given numbers.
def find_gcd(a, b):
    # TODO: Your code here
    return


# Power of a Number
# Write a program that calculates the result of raising a number to a given power (both inputs provided by the user).
def calculate_power(base, exponent):
    # TODO: Your code here
    return


# List Reversal
# Create a program that reverses a list without using any built-in functions.
def reverse_list(input_list):
    # TODO: Your code here
    return


# Remove Duplicates
# Write a program that removes duplicates from a list while preserving the order of the original list.
def remove_duplicates(input_list):
    # TODO: Your code here
    return


# Count Vowels and Consonants
# Implement a program that counts the number of vowels and consonants in a given string (case-insensitive).
def count_vowels_and_consonants(input_string):
    # Convert the input string to lowercase for case-insensitive comparison
    # TODO: Your code here
    return


# Prime Number Generator
# Write a program that generates and prints a list of prime numbers within a given range.
def is_prime(number):
    # TODO: Your code here
    return


def generate_primes_in_range_slow(start, end):
    # TODO: Your code here
    return


# Palindrome List
# Write a program that takes a list of strings as input and returns a new list containing only the palindromes from the original list.
def filter_palindromes(word_list):
    # TODO: Your code here
    return


# Fibonacci Sequence
# Create a program that generates and prints the first n numbers in the Fibonacci sequence, where n is given as input.
def generate_fibonacci_sequence(n):
    # TODO: Your code here
    return


# Anagram Checker
# Implement a program that checks if two strings are anagrams of each other (i.e., they have the same characters in different orders).
def are_anagrams(str1, str2):
    # TODO: Your code here
    return


# Matrix Transposition
# Write a program that transposes a given matrix (2D list), switching rows with columns.
def transpose_matrix(matrix):
    # TODO: Your code here
    return


# Factorization
# Create a program that factors a given positive integer and prints its prime factors.
def factor_integer(n):
    # TODO: Your code here
    return


# Reverse Words in a Sentence
# Write a program that reverses the words in a sentence. For example, "Hello, World!" should become "World! Hello,".
def reverse_words(sentence):
    # TODO: Your code here
    return


# List Intersection
# Implement a program that finds and prints the common elements between two lists.
def find_common_elements(list1, list2):
    # TODO: Your code here
    return


# Decimal to Binary Converter
# Create a program that converts a decimal number to its binary representation.
def decimal_to_binary(decimal):
    # TODO: Your code here
    return


# Sum of Squares vs. Square of Sum
# Write a program that calculates and prints the difference between the sum of squares and the square of the sum of the first n natural numbers, where n is given as input.
def sum_of_squares(n):
    # TODO: Your code here
    return


def square_of_sum(n):
    # TODO: Your code here
    return


# Email Validator
# Implement a program that checks if a given string is a valid email address based on a simple set of rules (e.g., it contains an "@" symbol and a "." character in the right positions).
def is_valid_email(email):
    # TODO: Your code here
    return


# Pascal's Triangle
# Write a program that generates and prints the first n rows of Pascal's Triangle, where n is given as input.
def generate_pascals_triangle(n):
    # TODO: Your code here
    return


def print_pascals_triangle(triangle):
    # TODO: Your code here
    return


# Matrix Multiplication
# Create a program that performs matrix multiplication for two given matrices and prints the result.
def matrix_multiply(matrix1, matrix2):
    # TODO: Your code here
    return


def print_matrix(matrix):
    # TODO: Your code here
    return


# Common Characters in Strings
# Write a program that finds and prints the common characters between two strings (case-sensitive).
def find_common_characters(string1, string2):
    # TODO: Your code here
    return


# Armstrong Number Checker
# Implement a program that checks if a given number is an Armstrong number. An Armstrong number is one where the sum of its own digits, each raised to the power of the number of digits, is equal to the number itself.
def is_armstrong_number(number):
    # TODO: Your code here
    return


# String Compression
# Create a program that compresses a given string by replacing consecutive duplicate characters with the character followed by the count.
# Count should NOT be omitted even if it is 1.
def compress_string(input_string):
    # TODO: Your code here
    return


# String Compression 2
# Create a program that compresses a given string by replacing consecutive duplicate characters with the character followed by the count.
# Count should be omitted if it is 1.
def compress_string2(input_string):
    # TODO: Your code here
    return


# Count Substrings
# Create a program that counts the occurrences of a given substring within a larger string.
# You may use standard library functions.
def count_substring_occurrences(full_string, substring):
    # TODO: Your code here
    return


# Largest Palindrome Product
# Write a program that finds and prints the largest palindrome that is a product of two three-digit numbers.
def find_largest_palindrome_product():
    # TODO: Your code here
    return


# Sum of Primes
# Create a program that calculates and prints the sum of all prime numbers below a given limit.
def sum_primes_below_limit(limit):
    # TODO: Your code here
    return


# Quadratic Equation Solver
# Write a program that takes coefficients (a, b, and c) of a quadratic equation as input and calculates its real roots using the quadratic formula.
def calculate_quadratic_roots(a, b, c):
    # TODO: Your code here
    return


# Remove Duplicates from Sorted Array
# Implement a program that removes duplicates from a sorted list in-place and returns the new length of the modified list.
def remove_duplicates(nums):
    # TODO: Your code here
    return


# Vigenère Cipher
# Implement a program that encrypts and decrypts messages using the Vigenère cipher. Allow the user to input a keyword for encryption and decryption.
def vigenere_encrypt(plain_text, keyword):
    # TODO: Your code here
    return


def vigenere_decrypt(encrypted_text, keyword):
    # TODO: Your code here
    return


# Caesar Cipher
# Create a program that encrypts and decrypts messages using a Caesar cipher. Allow the user to specify the shift value.
def caesar_encrypt(text, shift):
    # TODO: Your code here
    return


def caesar_decrypt(text, shift):
    # TODO: Your code here
    return
