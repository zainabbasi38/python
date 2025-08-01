# Calculater
first_number = int(input("Enter your first number: "))
second_number = int(input("Enter your second number: "))

operations = input("What operation you will perform (+ , - , * , / )? ")
if operations == "+":
    sum = first_number + second_number
    print(f"{first_number} + {second_number} is equal to", sum)
elif operations == "-":
    subtract = first_number - second_number
    print(f"{first_number} - {second_number} is equal to", subtract)
elif operations == "*":
    multiply = first_number * second_number
    print(f"{first_number} * {second_number} is equal to", multiply)
elif operations == "/":
    division = first_number / second_number
    print(f"{first_number} / {second_number} is equal to", division)

else:
    print("This operation is not allowed.")