def Sum(n):
    if (n == 1): return 1
    return n + Sum(n-1)

n = int(input("Nhập n: "))
print(Sum(n))