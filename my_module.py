def greeting(name):
    print("Hello, " + name + "!")

def calculate_square(num):
    return num * num

def calculate_factorial(num):
    factorial = 1
    for i in range(1, num + 1):
        factorial *= i
    return factorial

def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            return False
    return True