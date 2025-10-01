while True:
    try:
        Num = float(input("Enter a number: "))
        print(f"You entered {Num}")
        break  
    except ValueError:
        print("Invalid input. Please enter a valid integer/Float number.")
