def Sort(A, n):
    for i in range(0, n):
        # Lưu giá trị và vị trí nhỏ nhất 
        i_min = i
        v_min = A[i]
        for j in range(i, n): # Để bỏ qua các giá trị ở đầu đã sắp xếp
            if (A[j] < v_min):
                v_min = A[j]
                i_min = j
        # Đổi vị trí với i 
        A[i], A[i_min] = A[i_min], A[i]
A = [12, 234, 11, 5, 50, 200]
n = len(A)
Sort(A, n)
print(A)