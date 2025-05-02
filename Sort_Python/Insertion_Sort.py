def Insertion(A):
    n = len(A)
    for i in range(1,n):
        j = i
        while (j > 0 and A[j] < A[j-1]):
            # Hoán đổi vị trí
            A[j], A[j - 1] = A[j - 1], A[j]
            j = j - 1
n = int(input("Nhập số lượng phần tử của mảng: "))
A = []
for i in range(n): 
    A.append(int(input(f"Nhập phần tử thứ {i} của mảng: ")))
Insertion(A)
print(A)