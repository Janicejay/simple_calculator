while True:
    num1 = int(input("Enter the first number (or 'q' to quit): "))
    
    if num1 == 'q':
        break
    
    operator = input("Enter an operator (+, -, *, /): ")
    num2 = int(input("Enter the second number: "))

    if operator == '+':
        result = num1 + num2
    elif operator == '-':
        result = num1 - num2
    elif operator == '*':
        result = num1 * num2
    elif operator == '/':
        if num2 != 0:
            result = num1 / num2
        else:
            print("Error: Division by zero is not allowed.")
            continue
    else:
        print("Error: Invalid operator.")
        continue

    print("Result: %s" % result)
