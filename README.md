Python Error Handling Exercises

A set of practice exercises to build familiarity with Python's exception handling features.

---

## Exercise 1 — Basic Try-Except
**Problem:** Write a program that asks the user for two numbers and divides them. Handle the `ZeroDivisionError` if the second number is zero.

---

## Exercise 2 — Multiple Exception Handling
**Problem:** Create a program that accesses an element from a list based on user input. Handle both `IndexError` and `ValueError`.

---

## Exercise 3 — Else Clause
**Problem:** Write a program that demonstrates the use of the `else` clause in a try-except block. The `else` should run when no exception occurs (for example, after successfully opening and reading input).

---

## Exercise 4 — Finally Clause
- **Problem 1:** Write a program that tries to open and read a file. Use the `else` clause to print a success message if no exceptions occur.
- **Problem 2:** Create a program that demonstrates the use of the `finally` clause. The `finally` block should execute regardless of whether an exception occurred.

---

## Exercise 5 — Custom Exception
**Problem:** Create a custom exception for age validation. Raise this exception if the entered age is negative.

---

## Exercise 6 — Comprehensive Error Handling
**Problem:** Write a program that handles multiple potential errors in a simple banking application (for example: invalid input, insufficient funds, account not found).

---

## Exercise 7 — Nested Try-Except
**Problem:** Create a program with nested try-except blocks to handle different levels of errors (e.g., file I/O errors at outer level, parsing errors at inner level).

---

## Exercise 8 — Retry Mechanism
**Problem:** Implement a retry mechanism that allows the user to try again when they enter invalid input. The program should limit the number of attempts and handle exceptions cleanly.

---

## Practice Tips

- **Start Simple:** Begin with basic try-except blocks.
- **Test Different Scenarios:** Always test your code with both valid and invalid inputs.
- **Be Specific:** Catch specific exceptions rather than using bare `except:` clauses.
- **Use Meaningful Messages:** Provide helpful error messages to users.
- **Practice Regularly:** Error handling improves with consistent practice.

### Common Python Exceptions to Know
- `ValueError`: Invalid value
- `TypeError`: Wrong type used
- `IndexError`: List index out of range
- `KeyError`: Dictionary key not found
- `FileNotFoundError`: File doesn't exist
- `ZeroDivisionError`: Division by zero
- `ImportError`: Module import failed

---

These exercises will help you build confidence in handling errors effectively.
