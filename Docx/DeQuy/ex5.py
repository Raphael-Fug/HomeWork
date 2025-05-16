def gcd(a, b):
    if (b == 0): return a
    return gcd(b, a%b)
a = int(input("Nhập a: "))
b = int(input("Nhập b: "))
if (a > b):
    print(gcd(a,b))
else:
    a, b = b, a
    print(gcd(a,b))
