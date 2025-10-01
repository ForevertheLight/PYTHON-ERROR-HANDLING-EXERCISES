# Custom Exceptions
class NegativeAgeError(Exception):
    pass

class UnderageError(Exception):
    pass

class CitizenshipError(Exception):
    pass


# Function to validate voter
def validate_voter(Age, Citizenship):
    # Check for negative age
    if Age < 0:
        raise NegativeAgeError

    # Check for minimum age requirement
    if Age < 18:
        raise UnderageError

    # Check for citizenship
    if Citizenship!="Nigerian":
        raise CitizenshipError
    else:
        print("Congratulations! You can now Vote!")
    

    

#Using the Validate Voter Function 
try:
    Age = int(input("Enter your age: "))
    Citizenship= str(input("Enter Your Citizenship: "))
    validate_voter(Age, Citizenship)
except NegativeAgeError:
    print("Age Cannot be Negative")
except UnderageError:
    print("You must be 18years and Above")
except CitizenshipError:
    print("You must be a Nigerian to Vote")
