def calculator():
    op = input("Enter operation (+, -, *, /): ")
    a = float(input("Enter first number: "))
    b = float(input("Enter second number: "))

    if op == '+':
        print(f"{a} + {b} = {a + b}")
    elif op == '-':
        print(f"{a} - {b} = {a - b}")
    elif op == '*':
        print(f"{a} * {b} = {a * b}")
    elif op == '/':
        if b != 0:
            print(f"{a} / {b} = {a / b}")
        else:
            print("Error: Division by zero is not allowed.")
    else: 
        print("Error: Invalid operation. Please enter one of +, -, *, /.")

calculator()
input("Press Enter to exit the program...")