# def Fibo(n):
#     if (n <= 2): return 1
#     return Fibo(n-2) + Fibo(n-1)
# n = int(input("Nhập n: "))
# def GiaiThua(n):
#     if (n == 0 or n == 1): return 1
#     return GiaiThua(n-1)*n
# def Max(A, L, R):
#     m = len(A)/2
#     if (L == R): return A[L]
#     return Max()

# print(Fibo(n))
def Selection_Sort(A, n):
    for i in range(n):
        for j in range(i+1, n):
            if A[i] > A[j]:
                A[i], A[j] = A[j], A[i]
A = [12, 234, 11, 5, 50, 200]
n = len(A)
Selection_Sort(A, n)
print(A)