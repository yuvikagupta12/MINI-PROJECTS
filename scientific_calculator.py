import math

while True:
    print("\n===== SCIENTIFIC CALCULATOR =====")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Square Root")
    print("6. Power")
    print("7. Sin")
    print("8. Cos")
    print("9. Tan")
    print("10. Log")
    print("11. Exit")

    choice = input("Enter your choice: ")

    try:
        if choice == "1":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result =", a + b)

        elif choice == "2":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result =", a - b)

        elif choice == "3":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            print("Result =", a * b)

        elif choice == "4":
            a = float(input("Enter first number: "))
            b = float(input("Enter second number: "))
            if b == 0:
                print("Cannot divide by zero!")
            else:
                print("Result =", a / b)

        elif choice == "5":
            a = float(input("Enter number: "))
            print("Result =", math.sqrt(a))

        elif choice == "6":
            a = float(input("Enter base: "))
            b = float(input("Enter power: "))
            print("Result =", math.pow(a, b))

        elif choice == "7":
            a = float(input("Enter angle in degrees: "))
            print("Result =", math.sin(math.radians(a)))

        elif choice == "8":
            a = float(input("Enter angle in degrees: "))
            print("Result =", math.cos(math.radians(a)))

        elif choice == "9":
            a = float(input("Enter angle in degrees: "))
            print("Result =", math.tan(math.radians(a)))

        elif choice == "10":
            a = float(input("Enter number: "))
            print("Result =", math.log10(a))

        elif choice == "11":
            print("Calculator Closed")
            break

        else:
            print("Invalid Choice!")

    except ValueError:
        print("Please enter valid numbers.")