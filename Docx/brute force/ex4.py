def GhiNhan(A):
    for i in range(len(A)):
        print(A[i], end=' ')  # In cùng trên một dòng
    print()
    
def HoanVi(A, k):
    if k == len(A):
        GhiNhan(A)
    else:
        for i in range(k, len(A)):
            A[k], A[i] = A[i], A[k]  # Hoán đổi
            HoanVi(A, k + 1)
            A[k], A[i] = A[i], A[k]  # Hoán đổi lại để quay về trạng thái ban đầu
A = []
n = int(input("Nhập số lượng phần tử của mảng: "))
for i in range(0, n):
    i = int(input(f"Nhập phần tử thứ {i} của mảng: "))
    A.append(i)
HoanVi(A, 0)