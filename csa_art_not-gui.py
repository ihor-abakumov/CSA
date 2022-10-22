# Generated list randome symbols (digits&letter)

import random

def fn_create_random_string (list_range):
    """Function generated list randome symbols (digits&letter)"""
    string_random = ''
    for i in range(list_range):
        string_random = string_random + random.choice(list("""123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"""))
    return list(string_random)


list_random_any_symbols = fn_create_random_string (int(input("Enter the number of characters: ")))
    # Variable list randome symbols (digits&letter) - et by the user long

# Calculation of the execution time

# Selecting the sorting method

# Sorting methods

# Result work sorting method