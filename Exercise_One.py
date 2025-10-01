# Program to divide two numbers with error handling

# Ask the user for input
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

try:
    result = num1 / num2
    round(result,2)
    print(f"The result of {num1} ÷ {num2} is: {result}")
except ZeroDivisionError:
    print("Error: You cannot divide by zero!")
