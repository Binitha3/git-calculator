print("Calculator")
print("----------")

print("1. Basic Calculator")
print("2. Simple Interest")
print("3. Compound Interest")

choice = input("Choose an option: ")

if choice == "1":

    num1 = float(input("Enter first number: "))
    operator = input("Enter operator (+, -, *, /): ")
    num2 = float(input("Enter second number: "))

    if operator == "+":
        result = num1 + num2

    elif operator == "-":
        result = num1 - num2

    elif operator == "*":
        result = num1 * num2

    elif operator == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Cannot divide by zero"

    else:
        result = "Invalid operator"

    print("Result:", result)


elif choice == "2":

    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    time = float(input("Enter time (years): "))

    simple_interest = (principal * rate * time) / 100

    print("Simple Interest:", simple_interest)
    print("Total Amount:", principal + simple_interest)


elif choice == "3":

    principal = float(input("Enter principal amount: "))
    rate = float(input("Enter annual interest rate (%): "))
    time = float(input("Enter time (years): "))

    amount = principal * (1 + rate / 100) ** time
    compound_interest = amount - principal

    print("Compound Interest:", compound_interest)
    print("Total Amount:", amount)


else:
    print("Invalid choice")