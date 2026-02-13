# how to make a calculator in python
# this is a simple calculator that can perform basic arithmetic operations

num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operation = input("Enter operation (+, -, *, /,^): ")

if operation == "+":
    result = num1 + num2
    print("Result: ", result)
elif operation == "-":
    result = num1 - num2
    print("Result: ", result)
elif operation == "*":
    result = num1 * num2
    print("Result: ", result)
elif operation == "/":
    if num2 != 0:   # check for division by zero because it is not allowed in mathematics
        result = num1 / num2
        print("Result: ", result)
    else:
        print("Error: Division by zero is not allowed.")
elif operation == "^":
    result = num1 ** num2
    print("Result: ", result)
else:
    print("Error: Invalid operation.")