def Fibo(n):
    if (n <= 2): return 1
    return Fibo(n-2) + Fibo(n-1)
n = int(input("Nhập n: "))
def GiaiThua(n):
    if (n == 0 or n == 1): return 1
    return GiaiThua(n-1)*n
def Max(A, L, R):
    m = len(A)/2
    if (L == R): return A[L]
    return Max()

print(Fibo(n))