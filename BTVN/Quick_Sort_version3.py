def Partition(A, left, right):
    Key = A[(left + right)//2]
    i = left -1
    for j in range(left, right+1):
        if(A[j] < Key):
            i += 1
            A[i], A[j] = A[j], A[i]
    A[i+1], A[(left + right)//2] = A[(left + right)//2], A[i+1]
    return i + 1
def Sort(A, left, right):
    if (left < right):
        Key = Partition(A, left, right)
        Sort(A, left, Key - 1)
        Sort(A, Key + 1, right)
A = [12, 234, 11, 5, 50, 200]
n = len(A)
Sort(A, 0, n - 1)
print(A)