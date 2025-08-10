# A simple calculator program that performs basic arithmetic operations

# Ask the user to enter the first number 
num1 = float(input("Enter first number: "))

# Ask the user to enter the operation they want to perform
operation = input("Enter operation (+, -, *, /): ")

# Ask the user to enter the second number
num2 = float(input("Enter second number: "))
# Perform the operation based on user input

if operation == '+':
    result = num1 + num2
elif operation == '-':
    result = num1 - num2
elif operation == '*':
    result = num1 * num2
elif operation == '/':
    if num2 != 0:
        result = num1 / num2
# Handle division by zero
    else:
        result = "Error: Division by zero is not allowed."
    
# Check if the operation is valid
elif operation not in ['+', '-', '*', '/']:
    result = "Error: Invalid operation."
else:
    result = "Error: Invalid operation."
# Display the result to the user

print("Result:", result) 


