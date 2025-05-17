n = int(input())
A = [0]*n
def InKQ():
    for item in range(n):
        print(A[item], end=" ")
    print()
def Try(i):
    for j in range(0, 2):
        A[i] = j
        if (i == n-1): InKQ()
        else:
            Try(i+1)
Try(0)