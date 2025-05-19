def MergeSort(A, n, p, r):
    if (p < r):
        #Kiểm tra 
        q = (p + r) // 2
        # Chia để trị
        MergeSort(A, n, p, q)
        MergeSort(A, n, q+1, r)
        Merge(A, n, p, q, r)
def Merge(A, n, p, q, r):
    B = [0]*(r - p + 1)
    k = 0
    i = p
    j = q + 1
    # Tách ra sắp xếp
    while(i <= q and j <= r):
        if(A[i] < A[j]):
            B[k] = A[i]
            k += 1
            i += 1
        else:
            B[k] = A[j]
            k += 1
            j += 1
    # Trường hợp bên i vẫn còn
    while(i <= q):
        B[k] = A[i]
        k += 1
        i += 1
    # Trường hợp bên j vẫn còn
    while(j <= r):
        B[k] = A[j]
        k += 1
        j += 1
    # Sao chép từ B vào A
    for i in range(len(B)):
        A[p + i] = B[i]
A = [12, 234, 11, 5, 50, 200]
n = len(A)
MergeSort(A, n, 0, n-1)
print(A)