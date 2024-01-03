import os

# TODO: Implement read_file
def read_file(filename):
    with open(filename, 'r') as file:
        return file.read()

# TODO: Implement write_file
def write_file(filename, content):
    with open(filename, 'w') as file:
        file.write(content)

# TODO: Implement append_to_file
def append_to_file(filename, content):
    with open(filename, 'a') as file:
        file.write(content)

# TODO: Implement file_exists
def file_exists(filename):
    return os.path.exists(filename)

