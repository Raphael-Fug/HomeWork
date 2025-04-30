def Sentinel(A, K):
    n = len(A)
    A = A.append(K)
    i = 0
    while A[i] != K :
        i = i + 1
    if (i < n + 1): return i
    else: return -1
n = int(input("Nhập số lượng phần tử của mảng: "))
A = []
for i in range(n): 
    A.append(int(input(f"Nhập phần tử thứ {i} của mảng: ")))
K = int(input("Nhập phần tử cần tìm: "))
print(Sentinel(A, K))