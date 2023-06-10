# i=0
# while i<=5:
#     print("*" * i)
#     i+=1

sum = 0
number = None
print("enter numbers to calculate to their sum, enter 0 to exit")
while number !=0:
    number = int(input("enter a number"))
    sum += number
print(f"sum: {sum}")
