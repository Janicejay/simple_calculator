def add(num1, num2):
    answer = num1 + num2
    print(str(num1) + "+" + str(num2) + "=" + str(answer))

def sub(num1, num2):
    answer = num1 - num2
    print(str(num1) + "-" + str(num2) + "=" + str(answer))

def mul(num1, num2):
    answer = num1 * num2
    print(str(num1) + "*" + str(num2) + "=" + str(answer))

def div(num1, num2):
    answer = num1 / num2
    print(str(num1) + "/" + str(num2) + "=" + str(answer))

while True:
    print("A, Addition")
    print("B, Subtraction")
    print("C, Multiplication")
    print("D, Division")
    print("E, Exit")

    option = input("input an option: ")

    if option == "a" or option == "A":
        print("Addition")
        num1 = int(input("input first number:"))
        num2 = int(input("input second number: "))
        add(num1, num2)
    elif option == "b" or option == "B":
        print("Subtraction")
        num1 = int(input("input first number:"))
        num2 = int(input("input second number: "))
        sub(num1, num2)
    elif option == "c" or option == "C":
        print("Multiplication")
        num1 = int(input("input first number:"))
        num2 = int(input("input second number: "))
        mul(num1, num2)
    elif option == "d" or option == "D":
        print("Division")
        num1 = int(input("input first number:"))
        num2 = int(input("input second number: "))
        div(num1, num2)
    elif option == "e" or option == "E":
        print("End")
        quit()
