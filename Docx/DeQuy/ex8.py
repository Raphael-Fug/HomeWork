def Ten2Two(n):
    if (n <= 1): return str(n)
    return str(n%2) + Ten2Two(n//2)
n = int(input("Nhập n: "))
print(Ten2Two(n))