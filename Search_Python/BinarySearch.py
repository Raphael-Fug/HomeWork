import math
def Binary(A, K):
    left = 0
    right = len(A)
    while (left <= right):
        mid = math.floor((left + right) / 2)
        if A[mid] == K : return mid
        elif A[mid] > K : right = mid - 1
        else : left = mid + 1
    return -1
n = int(input("Nhập số lượng phần tử của mảng: "))
A = []
for i in range(n): 
    A.append(int(input(f"Nhập phần tử thứ {i} của mảng: ")))
K = int(input("Nhập phần tử cần tìm: "))
print(Binary(A, K))