num = float(input("enter a number to check: "))

if num > 0:
    print("the number is positive.")
else:
    if num < 0:
        print("the number is negative.")
    else:
        print("the number is zero.")

if num % 2 == 0:
    print("the number is even.")
else:
    print("the number is odd.")
