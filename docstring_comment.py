def add_numbers(a, b):
    """ this function adds to number"""
    if a<0 or b<0:
        return "both values must be positive"
    result = a+b
    return result

print(add_numbers(4, 4))
