rows = int(input("enter number of rows: "))

print("pattern 1:")
for i in range(1, rows + 1):
    print("*" * i)

print("pattern 2:")
for i in range(rows, 0, -1):
    print("*" * i)

'''outputs:
*
**
***
'''
