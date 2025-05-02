def Selection(A):
    n = len(A)
    for i in range(0, n-1):
        i_min = i
        v_min = A[i]
        for j in range(i, n):
            if (A[j] < v_min):
                v_min = A[j]
                i_min = j
        A[i], A[i_min] = A[i_min], A[i]
n = int(input("Nhập số lượng phần tử của mảng: "))
A = []
for i in range(n): 
    A.append(int(input(f"Nhập phần tử thứ {i} của mảng: ")))
Selection(A)
print(A)
