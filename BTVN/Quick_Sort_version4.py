import random

A = [12, 234, 11, 5, 50, 200]
n = len(A)

def Partition(A, left, right):
    random_index = random.randint(1, n-1)
    Key = A[random_index]
    A[random_index], A[right] = A[right], A[random_index]
    i = left - 1
    for j in range(left, right):
        if (A[j] < Key):
            i +=1
            A[i], A[j] = A[j], A[i]
    A[i+1],A[right] = A[right], A[i+1]
    return i+1
def Sort(A, left, right):
    if left < right:
        Key = Partition(A, left, right)
        Sort(A, left, Key - 1)
        Sort(A, Key + 1, right)
Sort(A, 0, n - 1)
print(A)