import math
a = input("Nhập a: ")
b = input("Nhập b: ")
if (a == 0 and b == 0):
    print(f"{a}")
else:
    while (a != b):
        if (a > b): a = a - b
        else: b = b - a
    print(f"{a}")
    