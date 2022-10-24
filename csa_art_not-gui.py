# Generated list randome symbols (digits&letter)

import random

def fn_create_random_string (list_range_):
    """Function generated list randome symbols (digits&letter)"""
    string_random = ''
    for i in range(list_range_):
        string_random = string_random + random.choice(list("""123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"""))
    return list(string_random)


def fn_choice_5 (a=100, b=1000, c=10000, d=100000, f=1000000):
    """Function for the user 1 from the size of the list"""
    print("The number of elements in the list:")
    if type(a) == int:
        print ("1: " + str(a), "2: " + str(b), "3: " + str(c), "4: " + str(d), "5: " + str(f), sep='\n')
    if type(a) == str:
        print ("1: " + a, "2: " + b, "3: " + c, "4: " + d, "5: " + f, sep='\n')
    while True:
        try:
            var_choice = int(input('Select the number from 1 to 5: '))
            if var_choice == 1:
                return a
                break
            elif var_choice == 2:
                return b
                break
            elif var_choice == 3:
                return c
                break
            elif var_choice == 4:
                return d
                break
            elif var_choice == 5:
                return f
                break
            else:
                continue
        except ValueError as error:
            continue

list_range = fn_choice_5() # The size list
list_random_any_symbols = fn_create_random_string (list_range)
    # Variable list randome symbols (digits&letter) - et by the user long


# Selecting the sorting method

# Sorting methods

    
import timeit # Calculation of the execution time
start = timeit.default_timer()

list_random_any_symbols.sort() #Timsort - Python default

stop = timeit.default_timer()
execution_time = stop - start

# Result work sorting method
print("Timsort - ", str(list_range), " Executed in " + "[{:.8f}s]".format(execution_time)) #It returns time in sec