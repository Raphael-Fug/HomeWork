import math
def Jumb(A, K):
    n = len(A)
    step = round(math.sqrt(n))
    i = 0
    jumb = step + i
    while (jumb <= n and A[i] < K):
        jumb += step
        i += step
    if jumb > n : jumb = n
    while A[i] < K:
        i += 1
        if i > n or i > jumb:
            return -1
    if A[i] == K: return i
    else : return -1
n = int(input("Nhập số lượng phần tử của mảng: "))
A = []
for i in range(n): 
    A.append(int(input(f"Nhập phần tử thứ {i} của mảng: ")))
K = int(input("Nhập phần tử cần tìm: "))
print(Jumb(A, K))