
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

# TODO: Implement count_occurrences
def count_occurrences(string, character):
    """
    Returns the number of times a character occurs in a string.
    """
    count = 0
    for c in string:
        if c == character:
            count += 1
    return count

# TODO: Implement accumulate_even_numbers
def accumulate_even_numbers(limit):
    """
    Returns a list of even numbers up to a given limit (inclusive).
    """
    evens = []
    for i in range(2, limit + 1):
        if i % 2 == 0:
            evens.append(i)
    return evens
