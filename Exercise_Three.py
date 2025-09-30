# Program to open and read a file with exception handling

filename = input("Enter the filename to open: ")

try:
    with open(filename, "r") as file:
        content = file.read()
except FileNotFoundError:
    print("Error: File not found.")
else:
    print("File opened and read successfully!")
    print(content)
