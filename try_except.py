try:
    x = int(input("Enter a number."))
    result = 10/x
    print(x)
except ValueError:
    print("invalid input, enter only digit")
except ZeroDivisionError:
    print("number can not be devided by zero")
else:
    print("the result is:", result)
finally:
    print("Program execution complete.")