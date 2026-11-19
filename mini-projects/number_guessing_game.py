import random
x = 1
num = random.randint(1,100)
a = int(input("ENTER THE NUM: "))
while a != num:
    if a > num:
        print("It's too high")
    else:
        print("It's too low")
    x += 1
    a = int(input("ENTER THE NUM: "))
print("GUD! YOU GOT IT")
print("Attempts:", x)
