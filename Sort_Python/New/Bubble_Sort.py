def Sort(A, n):
    for i in range(n):
        count = 0
        for j in range(n - i -1): #Chỉ -i là nhũng giá trị đã được sắp xếp rồi
            if (A[j] > A[j+1]):
                A[j], A[j+1] = A[j+1], A[j]
                count += 1
            if count == 0: break

A = [12, 234, 11, 5, 50, 200]
n = len(A)
Sort(A, n)
print(A)
# O(n^2)