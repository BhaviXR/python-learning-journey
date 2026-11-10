# Simple Python Calculator

# 1. ask the user to choose an operation
print("Select operation:")
print("1. Add")
print("2. Subtract")
print("3. Multiply")
print("4. Divide")

choice = input("enter choice (1/2/3/4): ")

# 2. get the two numbers from the user
num1 = float(input("enter first number: "))
num2 = float(input("enter second number: "))

# 3. perform the calculation based on the user's choice
if choice == '1':
    result = num1 + num2
    print("result:", num1, "+", num2, "=", result)

elif choice == '2':
    result = num1 - num2
    print("result:", num1, "-", num2, "=", result)

elif choice == '3':
    result = num1 * num2
    print("result:", num1, "*", num2, "=", result)

elif choice == '4':
    # check if the user is trying to divide by zero
    if num2 == 0:
        print("error! division by zero is not allowed.")
    else:
        result = num1 / num2
        print("result:", num1, "/", num2, "=", result)

else:
    print("invalid Input! Please choose a number from 1 to 4.")
