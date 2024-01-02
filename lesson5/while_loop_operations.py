
def find_first_divisible(target, divisor):
    """
    Find the first number greater than or equal to target that is divisible by divisor
    """
    number = target
    while number % divisor != 0:
        number += 1
    return number

# TODO: Implement accumulate_squares
def accumulate_squares(limit):
    """
    Return a list of the squares of numbers up to the given limit (inclusive)
    """
    squares = []
    number = 1
    while number**2 <= limit:
        squares.append(number**2)
        number += 1
    return squares

# TODO: Implement count_until_limit
def count_until_limit(string, character):
    """
    Count occurrences of a character in a string until reaching a limit of 10 occurrences
    """
    count = 0
    index = 0
    while count < 10 and index < len(string):
        if string[index] == character:
            count += 1
        index += 1
    return count

# TODO: Implement decrement_to_zero
def decrement_to_zero(number):
    """
    Create a list of numbers from the given number down to 0
    """
    sequence = []
    while number >= 0:
        sequence.append(number)
        number -= 1
    return sequence
