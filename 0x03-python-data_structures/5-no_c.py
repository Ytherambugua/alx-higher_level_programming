def no_c(my_string):
    new_string = ""
    for char in my_string:
        if char.lower() not in ['c']:
            new_string += char
    return new_string

print("Original string:", original_string)
print("String without 'c' and 'C':", result_string)
