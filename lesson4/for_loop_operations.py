def print_numbers(end):
    """
    Prints all numbers from 1 to end (inclusive).
    """
    for i in range(end):
        print(i + 1)

def print_numbers_reverse(end):
    """
    Prints all numbers from end to 1 (inclusive).
    """
    for i in range(end):
        print(end - i)

def print_numbers_even(end):
    """
    Prints all even numbers from 1 to end (inclusive).
    """
    for i in range(end):
        if (i + 1) % 2 == 0:
            print(i + 1)

def print_numbers_even_reverse(end):
    """
    Prints all even numbers from end to 1 (inclusive).
    """
    for i in range(end):
        if (end - i) % 2 == 0:
            print(end - i)

def sum_numbers(n):
    """
    Returns the sum of all numbers from 1 to n (including n).
    """
    total = 0
    for i in range(n):
        total += i + 1
    return total

def multiply_list(lst):
    """
    Returns the product of all elements in a list.
    """
    result = 1
    for element in lst:
        result *= element
    return result

def count_occurrences(string, character):
    """
    Returns the number of times a character occurs in a string.
    """
    count = 0
    for c in string:
        if c == character:
            count += 1
    return count

def accumulate_even_numbers(limit):
    """
    Returns a list of even numbers up to a given limit (inclusive).
    """
    evens = []
    for i in range(2, limit + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens

def find_min(numbers):
    """
    Returns the smallest number in a list.
    """
    min_num = numbers[0]
    for num in numbers:
        if num < min_num:
            min_num = num
    return min_num

def find_max(numbers):
    """
    Returns the largest number in a list.
    """
    max_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
    return max_num    

def max_min_diff(numbers):
    """
    Returns the difference between the largest and smallest numbers in a list.
    """
    max_num = numbers[0]
    min_num = numbers[0]
    for num in numbers:
        if num > max_num:
            max_num = num
        elif num < min_num:
            min_num = num
    return max_num - min_num

