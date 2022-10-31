import random
import timeit
import keyboard


# Generated list randome symbols - numbers & letter, numbers

def fn_create_random_string (list_range_):
    """Function generated list randome symbols (digits&letter)"""
    string_random = ''
    for i in range(list_range_):
        string_random = string_random + random.choice(list("""123456789qwertyuiopasdfghjklzxcvbnmQWERTYUIOPASDFGHJKLZXCVBNM"""))
    return list(string_random)

def fn_create_random_string_2 (list_range_):
    list_ = [random.randint(-list_range_,list_range_) for i in range (list_range_)]
    return list_

def fn_choice_5 (a=100, b=1000, c=10000, d=50000, f=100000):
    """Function for the user 1 from the size of the list"""
    if type(a) == int:
        print("The number of elements in the list:")
        print ("1: " + str(a), "2: " + str(b), "3: " + str(c), "4: " + str(d), "5: " + str(f), sep='\n')
    if type(a) == str:
        print("The number of algoritmes for test:")
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

# Algoritmes functions

def buble_sort(list_bs):
    """Function - Buble sort algoritm"""
    count_bs = 0
    for j in range (len(list_bs) - 1):
        for i in range (len(list_bs) - 1 - j):
            if list_bs[i] > list_bs[i+1]:
                count_bs += 1
                list_bs[i], list_bs[i+1] = list_bs[i+1], list_bs[i]
    return list_bs, count_bs

def quick_sort(list_qs):
    """Function - Quick sort algoritm"""
    if len(list_qs) <= 1:
        return list_qs
    elem_qs = list_qs [len(list_qs) // 2]
    left = list(filter(lambda x: x<elem_qs, list_qs))
    center = [i for i in list_qs if i==elem_qs]
    right = list(filter(lambda x: x>elem_qs, list_qs))
    return quick_sort(left) + center + quick_sort(right)


def merge_two_list (a,b):
    """Function - Merge two list"""
    c = []
    i = j = 0
    while i < len (a) and j < len (b):
        if a[i] < b[j]:
            c.append(a[i])
            i += 1
        else:
            c.append(b[j])
            j += 1
    if i < len (a):
        c += a [i:]
    if j < len (b):
        c += b [j:]
    return c

def merge_sort (list_ms):
    """Function - Merge sort algoritm"""
    if len(list_ms) == 1:
        return list_ms
    middle = len(list_ms) // 2
    left = merge_sort(list_ms[:middle])
    right = merge_sort(list_ms[middle:])
    return merge_two_list(left, right)


def shell_sort(list_ss):
    n = len(list_ss)
    step = n // 2
    while step > 0:
        for i in range (step, n):
            j = i
            while j >= step and list_ss [j] < list_ss[j-step]:
                list_ss[j], list_ss[j-step] = list_ss[j-step], list_ss[j]
                j =  j - step
        step = step // 2
    return list_ss



flag=True
while flag:
    # Основные выбранные элементы

    list_range = fn_choice_5() 
        # The size list
    list_random_any_symbols = fn_create_random_string_2 (list_range)
        # Variable list randome symbols (digits&letter) - et by the user long
    list_range_sort = fn_choice_5('Timsort','Bublesort','Quicksort','Mergesort','Shellsort') 
        # Выбор алгоритма сортировки
    # Algoritmes Calculate time
    start = timeit.default_timer()

    if list_range_sort == 'Timsort':
        sorted (list_random_any_symbols) # Timsort - Python default
    if list_range_sort == 'Bublesort':
        buble_sort (list_random_any_symbols) # Bublesort - optimasing classik
    if list_range_sort == 'Quicksort':
        quick_sort (list_random_any_symbols) # Quicksort - classik
    if list_range_sort == 'Mergesort':
        merge_sort (list_random_any_symbols) # Mergesort - classik
    if list_range_sort == 'Shellsort':
        shell_sort (list_random_any_symbols) # Shellsort - classik
    
    stop = timeit.default_timer()
    execution_time = stop - start

    # Result work sorting method
    print(list_range_sort, " - ", str(list_range), " Executed in " + "[{:.8f}s]".format(execution_time)) #It returns time in sec
    flag_ = input('Repeat?(Y/N)')
    flag = True if flag_ == 'Y' or flag_ == 'y' else False
