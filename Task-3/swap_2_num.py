def swap_numbers(a, b):
    print(f"Before swap: a = {a}, b = {b}")
    a, b = b, a
    print(f"After swap: a = {a}, b = {b}")
    return a, b

def swap_numbers_arithmetic(a, b):
    print(f"Before swap: a = {a}, b = {b}")
    a = a + b
    b = a - b
    a = a - b
    print(f"After swap: a = {a}, b = {b}")
    return a, b

def swap_numbers_xor(a, b):
    print(f"Before swap: a = {a}, b = {b}")
    a = a ^ b
    b = a ^ b
    a = a ^ b
    print(f"After swap: a = {a}, b = {b}")
    return a, b