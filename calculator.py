# calculator.py

# Simple calculator to add two numbers
# This script prompts the user for two numbers and prints their sum.
num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

sum = num1 + num2
print("The sum is:", sum)


# Simple calculator for basic arithmetic operations

# Get input from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Display operation choices
print("Choose the operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")

# Get user's choice
choice = input("Enter 1, 2, 3, or 4: ")

# Perform the chosen operation
if choice == "1":
    result = num1 + num2
    operation = "Addition"
elif choice == "2":
    result = num1 - num2
    operation = "Subtraction"
elif choice == "3":
    result = num1 * num2
    operation = "Multiplication"
elif choice == "4":
    if num2 != 0:
        result = num1 / num2
        operation = "Division"
    else:
        print("Error: Cannot divide by zero.")
        exit()
else:
    print("Invalid choice.")
    exit()

# Display the result
print(f"{operation} result: {result}")
