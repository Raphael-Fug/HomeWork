def Buble(A):
    n = len(A)
    for i in range(n-1):
        for j in range(n-1):
            if A[j] > A[j + 1]:
                A[j], A[j+1] = A[j+1], A[j]
n = int(input("Nhập số lượng phần tử của mảng: "))
A = []
for i in range(n): 
    A.append(int(input(f"Nhập phần tử thứ {i} của mảng: ")))
Buble(A)
print(A)                