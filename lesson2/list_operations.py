# TODO: Implement add_element
def add_element(input_list, element):
    """
    Adds an element to the end of the list.
    Returns the new list.
    """
    input_list.append(element)
    return input_list

# TODO: Implement remove_element
def remove_element(input_list, element):
    """
    Removes an element from the list.
    Returns the new list.
    """
    input_list.remove(element)
    return input_list

# TODO: Implement get_element
def get_element(input_list, index):
    """
    Returns the element at the given index.
    """
    return input_list[index]

# TODO: Implement modify_element
def modify_element(input_list, index, new_element):
    """
    Modifies the element at the given index with the new element.
    Returns the new list.
    """
    input_list[index] = new_element
    return input_list