def add_numbers(a, b):
    if a<0 or b<0:
        return "both values must be positive"
    result = a+b
    return result

print(add_numbers(4, 4))
