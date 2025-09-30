# Program to access an element from a list with error handling

# Sample list
My_List = ["Joshua",2004, "Christian", "Python", 21.3]
print(My_List)

try:
    # Ask user for an index
    List_index = int(input("Enter an index to access the list above: "))
    
    # Try to access the element
    print(f"Element at index {List_index} is: {My_List[List_index]}")

except ValueError:
    print("Error: Please enter a valid integer to access the List.")

except IndexError:
    print("Error: Index out of range.")
