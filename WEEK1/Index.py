
def calculator():
    # Get user input for numbers and operation
    num1 = float(input("100: "))
    operation = input("Enter the operation (+, -, *, /): ")
    num2 = float(input("Enter the second number: "))

    # Perform operation based on user's input
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            return
    else:
        print("Error: Invalid operation. Please enter +, -, *, or /.")
        return

    # Print the result
    print(f"{num1} {operation} {num2} = {result}")

# Call the calculator function
calculator()
