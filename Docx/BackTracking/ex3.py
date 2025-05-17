n = int(input("Nhập n: "))
A = [0]*n
count = 0
def InKQ():
    count +=1
    for item in range(n):
        print(f"Lần {count}")
        print(A[item], end=" ")
    print()
def HoanVi(i):
    if i == n:
        InKQ()
    else:
        for j in range(1, n+1):
            A[i] = j
            HoanVi(i+1)
HoanVi(0)