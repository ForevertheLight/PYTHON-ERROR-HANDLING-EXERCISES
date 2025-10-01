# Define custom exception
class NegativeAgeError(Exception):
    pass

# Function to validate age
def validate_age(age):
    if age < 0:
        raise NegativeAgeError
    else:
        print(f"You are {age} years old")

# Example usage
try:
    age = int(input("Enter your age: "))
    validate_age(age)
except NegativeAgeError:
    print("Age Cannot be Negative")