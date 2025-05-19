def Sort(A, n):
    for i in range(1, n):
        key = A[i]
        j = i -1
        # Di chuyển các phần tử lớn hơn key sang phải
        while j >= 0 and A[j] > key:
            A[j + 1] = A[j]  # Di chuyển phần tử sang phải
            j -= 1           # Giảm chỉ số j
        A[j + 1] = key
A = [12, 234, 11, 5, 50, 200]
n = len(A)
Sort(A, n)
print(A)