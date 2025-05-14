def Fibo(n):
    if (n <= 2): return 1
    return Fibo(n-2) + Fibo(n-1)
n = int(input("Nhập n: "))
print(Fibo(n))