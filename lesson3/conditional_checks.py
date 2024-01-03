def is_even(number):
    """
    Returns True if the number is even, False otherwise.
    """
    is_even = number % 2 == 0
    return is_even

# TODO: Implement greater_than_ten
def greater_than_ten(number):
    """
    Returns True if the number is greater than ten, False otherwise.
    """
    res = number > 10
    return res


def string_check(input_string):
    """
    Returns "Short String" if the string length is less than 10,
    "Long String" if it's 10 or more.
    """
    if len(input_string) < 10:
        str = "Short String"
    else: 
        str = "Long String"
    return str

def compound_condition(number, text):
    """
    Returns True if the number is less than 10 and the text contains "Python",
    False otherwise.
    """
    res = number < 10 and "Python" in text
    return res
