def Linear(A, K):
    n = len(A)
    for i in range(n):
        if (A[i] == K): return i
    return -1

n = int(input("Nhập số lượng phần tử của mảng: "))
A = []
for i in range(n): 
    A.append(int(input(f"Nhập phần tử thứ {i} của mảng: ")))
K = int(input("Nhập phần tử cần tìm: "))
print(Linear(A, K))