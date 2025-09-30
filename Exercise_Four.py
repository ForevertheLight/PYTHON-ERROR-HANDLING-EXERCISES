# Program to demonstrate the use of finally clause

try:
    number1 = int(input("Enter the first number: "))
    number2 = int(input("Enter the second number: "))
    result = number1 / number2
    print(f"Result: {round(result,2)}")

except ZeroDivisionError:
    print("Error: Cannot divide by zero.")

except ValueError:
    print("Error: Invalid input. Please enter numbers only.")

finally:
    print("Execution of the program is complete.")
