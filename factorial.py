#define the function

def factorial(n):
    # Check if n is negative
    if n < 0:
        raise ValueError("Error,number is negative numbers.")
    # Base case: factorial of 0 or 1 is 1
    elif n == 0 or n == 1:
        return 1
    # Recursive case
    else:
        return n * factorial(n - 1)

# Error Handling
try:
    number = int(input("Enter a number: "))
    result = factorial(number)
    print(f"The factorial of {number} is: {result}")
except ValueError as err:
    print(err)

